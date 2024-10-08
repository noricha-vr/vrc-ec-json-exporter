import {URL} from "url";
import https from "https";
import http from "http";

export const getGoogleForm = (url: string): Promise<string> => {
  return new Promise((resolve, reject) => {
    const parsedUrl = new URL(url);
    const protocol = parsedUrl.protocol === 'https:' ? https : http;

    protocol.get(parsedUrl, (response) => {
      let data = '';

      // ステータスコードが200台であることを確認
      if (response.statusCode && response.statusCode >= 200 && response.statusCode < 300) {
        response.setEncoding('utf8');
        response.on('data', (chunk) => data += chunk);
        response.on('end', () => resolve(data));
      } else if (response.headers.location) {
        // リダイレクトを処理
        getGoogleForm(response.headers.location).then(resolve).catch(reject);
      } else {
        reject(new Error(`リクエストが失敗しました。ステータスコード: ${response.statusCode}`));
      }
    }).on('error', (error) => reject(error));
  });
}