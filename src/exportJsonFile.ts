import * as fs from "node:fs";

/**
 * JSONファイルを出力する関数
 * @param data 出力するデータ
 * @param filename 出力するファイル名
 */
export const exportJsonFile = (data: Array<{ id: number; title: string }>, filename: string): void => {
  const outputData = {
    eventFormIdAndTitle: data
  };
  const jsonData = JSON.stringify(outputData, null, 2);
  fs.writeFileSync(filename, jsonData, 'utf8');
};
