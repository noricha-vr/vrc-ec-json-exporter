/**
 * HTMLからFB_PUBLIC_LOAD_DATA_の内容を抽出する関数
 * @param html 取得したHTML文字列
 * @returns FB_PUBLIC_LOAD_DATA_の内容をパースしたオブジェクトまたは配列
 */
export const extractFBPublicLoadData = (html: string): any => {
  // 正規表現でFB_PUBLIC_LOAD_DATA_の内容を抽出
  const regex = /var FB_PUBLIC_LOAD_DATA_ = (\[.*?\]);/s;
  const match = html.match(regex);

  if (match && match[1]) {
    const dataString = match[1];

    try {
      // 文字列をJSONに変換
      const data = JSON.parse(dataString);
      return data;
    } catch (error) {
      console.error('JSONのパースに失敗しました:', error);
      return null;
    }
  } else {
    console.error('FB_PUBLIC_LOAD_DATA_が見つかりませんでした。');
    return null;
  }
};


/**
 * HTMLからFB_PUBLIC_LOAD_DATA_の内容を抽出する関数
 * @param html 取得したHTML文字列
 * @returns FB_PUBLIC_LOAD_DATA_の内容をパースしたオブジェクトまたは配列
 */
/**
 * FB_PUBLIC_LOAD_DATA_ のデータから [ID, "タイトル"] を抽出する関数
 * @param data FB_PUBLIC_LOAD_DATA_ のデータ（配列）
 * @returns {id: number, title: string} の配列
 */
export const extractIdAndTitle = (data: any): Array<{ id: number; title: string }> => {
  const results: Array<{ id: number; title: string }> = [];

  const traverse = (node: any) => {
    if (Array.isArray(node)) {
      // 配列の最初の要素が数値、2番目の要素が文字列の場合
      if (
        typeof node[0] === 'number' &&
        typeof node[1] === 'string' &&
        node[1] !== null
      ) {
        results.push({ id: node[0], title: node[1] });
      }

      // 子要素を再帰的に探索
      for (const child of node) {
        traverse(child);
      }
    } else if (typeof node === 'object' && node !== null) {
      // オブジェクトの場合、その値を再帰的に探索
      for (const key in node) {
        traverse(node[key]);
      }
    }
    // それ以外の型（文字列、数値、null、undefined）の場合は何もしない
  };

  traverse(data);
  return results;
};
