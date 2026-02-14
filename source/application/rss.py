from datetime import datetime
from feedgen.feed import FeedGenerator
from typing import List, Dict
from ..translation import _

__all__ = ["RSS"]

# Constant for unavailable statistics values
UNAVAILABLE_VALUE = "-1"


class RSS:
    """RSS Feed Generator for Xiaohongshu content"""

    def __init__(self):
        self.base_url = "https://www.xiaohongshu.com"

    def generate_feed(
        self,
        items: List[Dict],
        title: str = None,
        description: str = None,
        link: str = None,
        author: str = None,
    ) -> str:
        """
        Generate RSS feed from a list of items

        Args:
            items: List of content items from Xiaohongshu
            title: Feed title
            description: Feed description
            link: Feed link
            author: Feed author name

        Returns:
            RSS feed as XML string
        """
        fg = FeedGenerator()
        
        # Set feed metadata
        fg.id(link or self.base_url)
        fg.title(title or _("小红书内容订阅"))
        fg.description(description or _("小红书作品 RSS 订阅"))
        fg.link(href=link or self.base_url, rel="alternate")
        fg.language("zh-cn")
        
        if author:
            fg.author({"name": author})

        # Add items to feed
        for item in items:
            self._add_item_to_feed(fg, item)

        return fg.rss_str(pretty=True).decode("utf-8")

    def _add_item_to_feed(self, fg: FeedGenerator, item: Dict) -> None:
        """Add a single item to the RSS feed"""
        fe = fg.add_entry()
        
        # Required fields
        item_id = item.get("作品ID", "")
        item_link = item.get("作品链接", f"{self.base_url}/explore/{item_id}")
        
        fe.id(item_link)
        fe.link(href=item_link)
        
        # Title
        title = item.get("作品标题", _("无标题"))
        fe.title(title or _("无标题"))
        
        # Description/Content
        description = item.get("作品描述", "")
        content = self._build_content(item)
        fe.description(description or _("无描述"))
        fe.content(content, type="html")
        
        # Author
        author_name = item.get("作者昵称", "")
        author_id = item.get("作者ID", "")
        author_link = item.get("作者链接", f"{self.base_url}/user/profile/{author_id}")
        
        if author_name:
            fe.author({
                "name": author_name,
                "uri": author_link
            })
        
        # Published date
        pub_date = item.get("发布时间", "")
        if pub_date and pub_date != _("未知"):
            try:
                # Parse datetime from format: "2024-01-01_12:00:00"
                dt = datetime.strptime(pub_date, "%Y-%m-%d_%H:%M:%S")
                fe.published(dt)
                fe.updated(dt)
            except (ValueError, TypeError):
                pass
        
        # Updated date
        update_date = item.get("最后更新时间", "")
        if update_date and update_date != _("未知") and update_date != pub_date:
            try:
                dt = datetime.strptime(update_date, "%Y-%m-%d_%H:%M:%S")
                fe.updated(dt)
            except (ValueError, TypeError):
                pass
        
        # Categories/Tags
        tags = item.get("作品标签", "")
        if tags:
            for tag in tags.split():
                fe.category(term=tag)

    def _build_content(self, item: Dict) -> str:
        """Build HTML content for RSS entry"""
        parts = []
        
        # Work type
        work_type = item.get("作品类型", "")
        if work_type:
            parts.append(f"<p><strong>{_('类型')}:</strong> {work_type}</p>")
        
        # Description
        description = item.get("作品描述", "")
        if description:
            parts.append(f"<p>{description}</p>")
        
        # Statistics
        stats = []
        if (likes := item.get("点赞数量")) and likes != UNAVAILABLE_VALUE:
            stats.append(f"{_('点赞')}: {likes}")
        if (collects := item.get("收藏数量")) and collects != UNAVAILABLE_VALUE:
            stats.append(f"{_('收藏')}: {collects}")
        if (comments := item.get("评论数量")) and comments != UNAVAILABLE_VALUE:
            stats.append(f"{_('评论')}: {comments}")
        if (shares := item.get("分享数量")) and shares != UNAVAILABLE_VALUE:
            stats.append(f"{_('分享')}: {shares}")
        
        if stats:
            parts.append(f"<p><strong>{_('数据')}:</strong> {' | '.join(stats)}</p>")
        
        # Tags
        tags = item.get("作品标签", "")
        if tags:
            parts.append(f"<p><strong>{_('标签')}:</strong> {tags}</p>")
        
        # Author
        author = item.get("作者昵称", "")
        author_link = item.get("作者链接", "")
        if author:
            parts.append(
                f'<p><strong>{_("作者")}:</strong> '
                f'<a href="{author_link}">{author}</a></p>'
            )
        
        # Work link
        work_link = item.get("作品链接", "")
        if work_link:
            parts.append(
                f'<p><a href="{work_link}">{_("查看原作品")}</a></p>'
            )
        
        return "\n".join(parts)

    def generate_user_feed(
        self,
        items: List[Dict],
        user_name: str = None,
        user_id: str = None,
    ) -> str:
        """
        Generate RSS feed for a specific user's content

        Args:
            items: List of user's content items
            user_name: User's nickname
            user_id: User's ID

        Returns:
            RSS feed as XML string
        """
        title = f"{user_name} - {_('小红书作品订阅')}" if user_name else _("用户作品订阅")
        description = f"{user_name}{_('的小红书作品订阅')}" if user_name else _("小红书用户作品订阅")
        link = f"{self.base_url}/user/profile/{user_id}" if user_id else self.base_url
        
        return self.generate_feed(
            items=items,
            title=title,
            description=description,
            link=link,
            author=user_name,
        )

    def generate_search_feed(
        self,
        items: List[Dict],
        keyword: str = None,
    ) -> str:
        """
        Generate RSS feed for search results

        Args:
            items: List of search result items
            keyword: Search keyword

        Returns:
            RSS feed as XML string
        """
        title = f"{keyword} - {_('小红书搜索订阅')}" if keyword else _("小红书搜索订阅")
        description = f"{keyword}{_('的搜索结果订阅')}" if keyword else _("小红书搜索结果订阅")
        link = self.base_url
        
        return self.generate_feed(
            items=items,
            title=title,
            description=description,
            link=link,
        )
