Store Token on Local Laptop
==============================================================================


Overview
------------------------------------------------------------------------------
作为开发者, 会需要调用各种软件服务商的 API. 一般软件服务商都是在你登陆之后, 允许你创建一个带有权限范围的 Token 用来代替账号密码进行鉴权. 然后你在 rest API 的请求中带上这个 token 既可. 但不是每个服务商的 token 都带有权限范围, 比如目前 GitHub 的 token 是有权限范围的, 但很多我用的其他服务是没有的.

一般你都需要将 token 保存到本地电脑的某个文件中, 然后在你的代码中去这个文件中读 (例如 GitHub 就是这样), 或是写入到某个特定的 config 文件中, 然后官方的 CLI 程序就会自动去这个文件中找 token (例如 PyPI 就是这样). 本文介绍了我所习惯的一套在本地电脑上存储这些 token 的方式. 通常它们都会被保存在 ``${HOME}`` (或 ``~``) 目录下的某个文件中.


PyPI
------------------------------------------------------------------------------
这是 Python 社区发布包的地方. 你在 https://pypi.org/manage/account/ 下可以看到创建 token 的选项. 它的 token 保存在 ``${HOME}/.pypirc`` 文件中. 例如 ``~/.pypirc``. 这是官方要求的而不是我自定义的, 如果你不按照这个文件名, 官方的 CLI 程序就找不到 token 了.


GitHub
------------------------------------------------------------------------------
这是大部分开源项目代码托管的地方. 你在 https://github.com/settings/tokens 下可以看到创建 token 的选项. 我习惯将 token 保存在 ``${HOME}/.github/pac/${GITHUB_USERNAME}/${TOKEN_NAME}.txt`` 文件中. 例如 ``~/.github/pac/MacHu-GWU/Full-Repo-Access.txt``.


CodeCov
------------------------------------------------------------------------------
这是一个代码覆盖率测试的服务商. 你在 https://app.codecov.io/account/${service}/${owner_username}/access 下可以看到创建 token 的选项, 例如 https://app.codecov.io/account/gh/MacHu-GWU/access. 我习惯将 token 保存在 ``${HOME}/.codecov/${SERVICE}/${OWNER_USERNAME}/${TOKEN_NAME}.txt`` 文件中. 例如 ``~/.codecov/github/MacHu-GWU/sanhe-dev.txt``.


ReadTheDocs
------------------------------------------------------------------------------
这是一个开源文档托管的服务商. 你在 https://readthedocs.org/accounts/tokens/ 下可以看到创建 token 的选项. 我习惯将 token 保存在 ``${HOME}/.readthedocs/${OWNER_USERNAME}/${TOKEN_NAME}.txt`` 文件中. 注意, Readthedocs 的 Owner Username 就是你 readthedocs 的 username, 而不是 GitHub 等代码仓库托管系统的 username. Readthedocs 官方没有 token name, 你要自己定义. 例如 ``~/.readthedocs/MacHu-GWU/sanhe-dev.txt``.


Google
------------------------------------------------------------------------------
`Google Cloud <https://cloud.google.com/>`_ 有一系列 API 可以控制各种 Google 产品例如 gmail, google drive 或者和 Google Cloud Service 联动. 由于 Google Account 下的管理方式一般是以 Project 为单位管理的, 并且通常有 OAuth Clients 和 Service Account 两种 Credentials, 我习惯将 token 用下面的目录结构进行保存:

.. code-block:: bash

    ${HOME}/.google/${Google_Account_Username_or_Alias}/${project_name}/
    ${HOME}/.google/${Google_Account_Username_or_Alias}/${project_name}/service_accounts/${Service_Account_Name_or_Alias}/keys/${key_name}.json
    ${HOME}/.google/${Google_Account_Username_or_Alias}/${project_name}/clients/${client_name_or_alias}/client_secret.json
    ${HOME}/.google/${Google_Account_Username_or_Alias}/${project_name}/clients/${client_name_or_alias}/client_token.json


Cloudflare
------------------------------------------------------------------------------
`Cloudflare <https://www.cloudflare.com/>`_ 是一个 CDN 服务商, 也是一个云计算服务提供商, 它提供了很多免费但是完全不差 AWS 的对标服务. 我习惯将 token 用下面的目录结构进行保存:

.. code-block:: bash

    ${HOME}/.cloudflare/${Cloudflare_Account_name_or_alias}/${key_type_such_as_api_token_r2_token_etc}/${key_name}.txt
