Duck(Strategyパターン)
============================

テキストとほぼ同じDuckでのStrategyパターンです

* Duckクラスは基底クラス
* Duckはflyとquackがサブクラスごとに挙動が異なる
* flyとquackはそれぞれbehaviorクラスを保持し、そちらで実装される
* それぞれの振る舞いは保持するbehaviorを差し替えることで動的に変更できる
