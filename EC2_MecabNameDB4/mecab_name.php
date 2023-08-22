<?php
// 文章
$text = "福岡県西方沖地震は、2005年3月20日、福岡県北西沖の玄界灘で発生したマグニチュード7.0、最大震度6弱の地震。震源に近い福岡市西区の玄界島で住宅の半数が全壊する被害となったのをはじめ、同区能古島、西浦、宮浦、東区志賀島などの沿岸地区で大きな被害となった。死者1名、負傷者約1,200名、住家全壊約140棟。福岡市付近では有史以来最も大きな地震となった。";

// MeCabオブジェクトの作成
$mecab = new MeCab\Tagger();

// 文章を解析してノードの配列を取得
$nodes = $mecab->parseToNode($text);

// 名詞のみを抽出して表示
foreach ($nodes as $n) {
    // 名詞の場合のみ表示
    $features = explode(',', $n->getFeature());
    if ($features[0] === '名詞') {
        echo $n->getSurface() . PHP_EOL;
    }
}
?>