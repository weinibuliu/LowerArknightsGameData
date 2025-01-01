## 轻量化明日方舟游戏数据 | LowerArknightsGameData

## 简介 | Introduction
本仓库旨在提供体积更小、针对性更强的明日方舟资源数据文件供其他场景使用。使用数据详见 **[数据来源](#数据来源--data-source)** 。

This repository aims to provide smaller and more targeted Arknights data and resource files for use in other scenarios. For details on the using data, see **[Data Source](#数据来源--data-source)** .

>[!WARNING]
仓库使用 **[Pygithub](https://github.com/PyGithub/PyGithub)** 获取 commit message ，如请求过于频繁，可能会触发 Github API 相关限制。请控制请求频率。\
\
The repository uses **[Pygithub](https://github.com/PyGithub/PyGithub)** to get commit messages. If the request is too frequent, it may trigger Github API related restrictions. Please control the request frequency.

## 发行版 | Release
>[!NOTE]
只要任一地区的游戏文件存在版本更新，就会创建发行版并将其标记为 **最新** 。因此，还需要校验具体地区的游戏文件对应的版本信息是否一致。它们存放于 `{language}-version` 文件中。\
\
Whenever there is a newer version of the game files for any region, a release is created and marked as **latest** . Therefore, it is also necessary to verify that the version information corresponding to the game files for specific regions is consistent. They are stored in the `{language}-version` file.

## 文件列表 | Files List
- `avatar` (干员头像)
- `character.json`（干员信息）

## 数据来源 | Data Source
本仓库使用了以下仓库的数据，感谢其维护者与贡献者的贡献。

This repository uses data from the following repositories.Thanks the contributions of their maintainers and contributors.

- **[MaaAssistantArknights](https://github.com/MaaAssistantArknights/MaaAssistantArknights)**

## 声明 | Statement
本仓库所有静态资源，版权均属于 **[明日方舟](https://ak.hypergryph.com)** 。本仓库仅出于学习与交流目的进行引用。

The copyright of all static resources in this repository belongs to **[Arknights](https://ak.hypergryph.com)**. This repository only quotes them for learning and communication.

## 致谢 | Acknowledgment
### 开源项目 | Repository

#### Github 工作流 | Github Workflows
- **[action-gh-release](https://github.com/softprops/action-gh-release)**
- **[checkout](https://github.com/actions/checkout)**
- **[release-downloader](https://github.com/robinraju/release-downloader)**
- **[setup-python](https://github.com/actions/setup-python)**

#### 开源库 | Library
- **[pygithub](https://github.com/PyGithub/PyGithub)**

#### 数据 | Data
- **[MaaAssistantArknights](https://github.com/MaaAssistantArknights/MaaAssistantArknights)**

### 贡献者 | Contributors
<a href="https://github.com/weinibuliu/LowerArknightsGameData/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=weinibuliu/LowerArknightsGameData&max=1000" />
</a>