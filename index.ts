import * as fs from 'fs';
import {extractFBPublicLoadData, extractIdAndTitle} from "./src/parseOutputHtml";
import {getGoogleForm} from "./src/getGoogleForm";
import {saveHTMLToFile} from "./src/saveHtml";
import {exportJsonFile} from "./src/exportJsonFile";


const outputFilePath = 'outputs/google-form.html';

// イベントカレンダーのGoogleフォームのURL
const url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSevo0ax6ALIzllRCT7up-3KZkohD3VfG28rcOy8XMqDwRWevQ/formResponse';

const main = async () => {

  const outputPageHTML = outputFilePath;

  await getGoogleForm(url)
    .then(html => {
      saveHTMLToFile(html, outputPageHTML);
      console.log(`HTMLが ${outputPageHTML} に保存されました`);
    })
    .catch(error => {
      console.error('HTMLのダウンロード中にエラーが発生しました:', error);
    });
  const htmlContent = fs.readFileSync(outputPageHTML, 'utf8');
  const dataList = extractFBPublicLoadData(htmlContent);
  const dataParams = extractIdAndTitle(dataList);
  exportJsonFile(dataParams);
  console.log('data-params属性の値:', dataParams);
  process.exit(0);
}

main().catch(console.error);

process.on('exit', () => {
  console.log('処理が完了しました');
});