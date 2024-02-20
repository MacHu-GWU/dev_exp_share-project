Chrome 高级技巧
==============================================================================
Chrome 系统 url

- 设定: chrome://settings/
- 浏览历史: chrome://history/
- 下载历史: chrome://downloads/
- 插件管理: chrome://extensions/
- 插件快捷键管理: chrome://extensions/shortcuts

Chrome 上有用的插件:

- LastPass: 密码管理
- Quick Tabs: 不用鼠标, 用全文搜索的方式跳转到打开的 Tab 中的一个.
- Adblock Plus: 广告屏蔽
- minterBlack: 加密货币挖矿代码屏蔽
- Bruce's Blank New Tab: 使得打开新标签时, 永远是空白页, 保护隐私
- Bookmark Sidebar: 颜值最高的标签管理器
- Grammarly for Chrome: 更正语法错误, 英语新手的福音


自定义 Chrome 插件的快捷键
------------------------------------------------------------------------------
打开 chrome://extensions/shortcuts 进入插件快捷键管理菜单进行编辑.

提高效率的一些快捷键:

- 跳转到地址栏: Ctrl + L (Windows), Cmd + L (Mac)
- 打开 Lastpass 搜索框: Shift + Cmd + L (Mac)
- 打开 Quick Tabs 搜索框: Cmd + E (Mac)


Google BookMark
------------------------------------------------------------------------------
Bookmark 书签页可能是我们使用最多的功能之一. 用一个友好的方式

- Q: 如何快速的搜索 Bookmark?
- A: 在搜索框中输入 ``@bookmarks`` 然后按 tab 或 空格 输入 query 进行搜索. 详情请参考 `Create, find & edit bookmarks in Chrome <https://support.google.com/chrome/answer/188842>`_, Google Help Center 的官方回答.


- Q: 我想对 Bookmark 的数据进行二次开发. 在哪里可以获得 bookmark 的数据?
- A: 根据 `Where are Google Chrome Bookmarks Stored on Computer? <https://www.ubackup.com/data-recovery-disk/where-are-google-chrome-bookmarks-stored.html>`_ 这篇博客, 在 Windows 下是 ``C:\Users\username\AppData\Local\Google\Chrome\User Data\Default``, 在 Mac 下是 ``/Users/username/Library/Application
 Support/Google/Chrome/Default``. 它里面是一个树状的 JSON 对象. 其中你的 bookmark 都在 ``bookmark_bar`` field 下. 里面的每个 item 可能是一个 ``{"name": "...", "url": "..."}`` 这样代表一个 bookmark 的对象, 也可能是一个 ``{"children": [...]}`` 这样代表一个文件夹的对象. 你可以自己写一段递归程序, 从而轻松地将数据抓出来.

.. code-block:: javascript

    {
        "checksum": "a1b2c3d4...",
        "roots": {
            "bookmark_bar": {...},
            "other": {},
            "synced": {}
        },
        "version": 1
    }
