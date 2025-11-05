# AnimeTrace 接口示例

这个目录集中存放了本次整理 AnimeTrace 识别接口时产出的脚本、数据和辅助资料，方便后续复用。

## 目录结构

- `call_animetrace.py`：调用 AnimeTrace `https://api.animetrace.com/v1/search` 接口的示例脚本，会读取同目录下的 `image_base64.txt` 并将响应写入 `animetrace_response.json`。
- `image_base64.txt`：测试图片的 Base64 数据，可直接替换为你自己的图片内容。
- `animetrace_response.json`：最近一次调用成功后保存的原始接口返回。
- `api_docs_test.txt`：接口文档关键参数、模型和错误码的速查笔记。
- `api_docs_chunk.js` / `api_docs_strings.json` / `parse_chunk.py`：用于解析官网前端打包文件、提取文案字段的辅助脚本和产物。
- `en_api_docs.html` / `en_api_docs.txt` / `extract_en_api_docs.py` / `chunk_0d37d38.js`：抓取并提取英文文档正文时留下的源码与脚本。

## 使用方式

1. 进入仓库根目录，执行：
   ```powershell
   & "E:\Downloads\MaiBotOneKey\runtime\python31211\bin\python.exe" animetrace_demo\call_animetrace.py
   ```
2. 如需更换测试图片，只要更新 `image_base64.txt` 的内容即可（建议保持 UTF-8 编码）。
3. 调用完成后，可直接打开 `animetrace_response.json` 查看识别结果；若需要解析其它文档片段，可运行同目录内的辅助脚本。

> **提示**：AnimeTrace 接口目前无需额外的 token 或密钥，如果未来官方有变动，记得同步更新脚本逻辑。
