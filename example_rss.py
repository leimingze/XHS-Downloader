# RSS 订阅功能使用示例
# RSS Feed Usage Examples

"""
XHS-Downloader RSS 订阅功能示例代码
Examples for using XHS-Downloader RSS feed functionality
"""

import requests
from urllib.parse import quote


def example_1_single_work_rss():
    """示例 1: 订阅单个作品
    Example 1: Subscribe to a single work
    """
    print("示例 1: 订阅单个作品")
    print("Example 1: Subscribe to a single work\n")
    
    # 小红书作品链接
    # Xiaohongshu work link
    work_url = "https://www.xiaohongshu.com/explore/65f1234567890abc"
    
    # RSS 订阅地址
    # RSS feed URL
    rss_url = f"http://127.0.0.1:5556/xhs/rss?url={quote(work_url)}"
    
    print(f"RSS 订阅地址 / RSS Feed URL:")
    print(rss_url)
    print()


def example_2_multiple_works_rss():
    """示例 2: 订阅多个作品
    Example 2: Subscribe to multiple works
    """
    print("示例 2: 订阅多个作品")
    print("Example 2: Subscribe to multiple works\n")
    
    # 多个作品链接（空格分隔）
    # Multiple work links (space-separated)
    work_urls = [
        "https://www.xiaohongshu.com/explore/65f1234567890abc",
        "https://www.xiaohongshu.com/explore/65f9876543210def",
        "https://www.xiaohongshu.com/explore/65fabcdef1234567",
    ]
    
    # 将多个链接组合为一个字符串
    # Combine multiple links into one string
    combined_urls = " ".join(work_urls)
    
    # RSS 订阅地址
    # RSS feed URL
    rss_url = f"http://127.0.0.1:5556/xhs/rss?url={quote(combined_urls)}"
    
    print(f"RSS 订阅地址 / RSS Feed URL:")
    print(rss_url)
    print()


def example_3_custom_feed_info():
    """示例 3: 自定义订阅标题和描述
    Example 3: Custom feed title and description
    """
    print("示例 3: 自定义订阅标题和描述")
    print("Example 3: Custom feed title and description\n")
    
    work_url = "https://www.xiaohongshu.com/explore/65f1234567890abc"
    title = "我的小红书收藏"
    description = "我收藏的小红书精选内容"
    
    # RSS 订阅地址
    # RSS feed URL
    rss_url = (
        f"http://127.0.0.1:5556/xhs/rss?"
        f"url={quote(work_url)}&"
        f"title={quote(title)}&"
        f"description={quote(description)}"
    )
    
    print(f"RSS 订阅地址 / RSS Feed URL:")
    print(rss_url)
    print()


def example_4_fetch_rss_feed():
    """示例 4: 获取 RSS 订阅内容
    Example 4: Fetch RSS feed content
    """
    print("示例 4: 获取 RSS 订阅内容")
    print("Example 4: Fetch RSS feed content\n")
    
    work_url = "https://www.xiaohongshu.com/explore/65f1234567890abc"
    rss_url = f"http://127.0.0.1:5556/xhs/rss?url={quote(work_url)}"
    
    try:
        # 请求 RSS 订阅
        # Request RSS feed
        response = requests.get(rss_url, timeout=30)
        
        if response.status_code == 200:
            print("✓ RSS 订阅获取成功 / RSS feed fetched successfully")
            print(f"内容长度 / Content length: {len(response.text)} 字符 / characters")
            print("\n前 500 个字符 / First 500 characters:")
            print(response.text[:500])
        else:
            print(f"✗ 获取失败 / Fetch failed: {response.status_code}")
    except Exception as e:
        print(f"✗ 错误 / Error: {e}")
    print()


def example_5_user_rss():
    """示例 5: 用户作品 RSS 订阅（占位符）
    Example 5: User works RSS feed (placeholder)
    """
    print("示例 5: 用户作品 RSS 订阅")
    print("Example 5: User works RSS feed\n")
    
    user_id = "test_user_123"
    
    # RSS 订阅地址
    # RSS feed URL
    rss_url = f"http://127.0.0.1:5556/xhs/user/rss?user_id={user_id}&limit=20"
    
    print(f"RSS 订阅地址 / RSS Feed URL:")
    print(rss_url)
    print("\n注意 / Note: 此功能当前为占位符实现，返回空订阅源")
    print("This is currently a placeholder implementation, returns empty feed")
    print()


def example_6_rss_reader_usage():
    """示例 6: 在 RSS 阅读器中使用
    Example 6: Using with RSS readers
    """
    print("示例 6: 在 RSS 阅读器中使用")
    print("Example 6: Using with RSS readers\n")
    
    print("常用 RSS 阅读器 / Popular RSS readers:")
    print("- Feedly (https://feedly.com)")
    print("- Inoreader (https://www.inoreader.com)")
    print("- NetNewsWire (https://netnewswire.com)")
    print("- Reeder (https://reederapp.com)")
    print("- Thunderbird (https://www.thunderbird.net)")
    print()
    
    print("使用步骤 / Usage steps:")
    print("1. 启动 XHS-Downloader API 服务器")
    print("   Start XHS-Downloader API server:")
    print("   python main.py api")
    print()
    print("2. 生成 RSS 订阅链接（见上面示例）")
    print("   Generate RSS feed URL (see examples above)")
    print()
    print("3. 将链接添加到 RSS 阅读器")
    print("   Add the URL to your RSS reader")
    print()
    print("注意 / Note:")
    print("- 确保 API 服务器保持运行")
    print("  Keep the API server running")
    print("- 本地访问请使用 127.0.0.1")
    print("  Use 127.0.0.1 for local access")
    print("- 远程访问需要配置防火墙和网络")
    print("  Remote access requires firewall and network configuration")
    print()


if __name__ == "__main__":
    print("=" * 70)
    print("XHS-Downloader RSS 订阅功能使用示例")
    print("XHS-Downloader RSS Feed Usage Examples")
    print("=" * 70)
    print()
    
    example_1_single_work_rss()
    print("-" * 70)
    
    example_2_multiple_works_rss()
    print("-" * 70)
    
    example_3_custom_feed_info()
    print("-" * 70)
    
    # 注释掉实际请求示例，避免在没有运行服务器时出错
    # Comment out actual request example to avoid errors when server is not running
    # example_4_fetch_rss_feed()
    # print("-" * 70)
    
    example_5_user_rss()
    print("-" * 70)
    
    example_6_rss_reader_usage()
    print("=" * 70)
