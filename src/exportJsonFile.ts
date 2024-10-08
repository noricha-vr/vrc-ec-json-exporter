import * as fs from "node:fs";

export const exportJsonFile = (idAndTitleList: any) => {
  fs.writeFile('eventDataParam.json', JSON.stringify(idAndTitleList, null, 2), 'utf8', (err) => {
    if (err) {
      console.error('ファイルの書き込みに失敗しました:', err);
    } else {
      console.log('データをeventDataParam.jsonに書き込みました。');
    }
  });

}
