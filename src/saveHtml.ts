import * as path from "node:path";
import * as fs from "node:fs";

/**
 * HTMLをファイルに保存する
 * @param html 保存するHTML文字列
 * @param filePath 保存先のファイルパス
 */
export const saveHTMLToFile = (html: string, filePath: string) => {
  const dir = path.dirname(filePath);

  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, {recursive: true});
  }

  fs.writeFileSync(filePath, html, 'utf8');
}

