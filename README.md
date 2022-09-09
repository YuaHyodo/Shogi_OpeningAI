# Shogi_OpeningAI
特定の囲いを組む将棋AI

# 概要
- 弱い将棋AIは、酷い序盤を指すため中終盤に苦しくなります。
- また、序盤でももかなり時間を消費するので、持ち時間の面でも苦しくなります。
- そんな弱い将棋AI達に代わって序盤を指し、特定の囲いを組むのがこのAIです。
- デフォルトでは「振り飛車穴熊」という囲いにしていますが、別の囲いにも簡単に変更できます。
- 囲いを組んでいる途中で攻撃されてもある程度なら対応できます。(多分)
- 探索を行っているので、定跡禁止環境でも使えます。

# 現在対応している囲い
- 1: 振り飛車穴熊
- 2: 美濃囲い

# 作ったきっかけ
- 単細胞くんというネタAIの序盤が酷かったのでそれを改善するためと、「超弱いAI同士では穴熊は最強説」を検証するため。

# 性能
- 単細胞くんv2(通常)の[floodgateでのレート](http://wdoor.c.u-tokyo.ac.jp/shogi/view/show-player.cgi?event=LATEST&filter=floodgate&show_self_play=1&user=tansaibo_kun_v2%2B81dc9bdb52d04dc20036dbd8313ed055)<br>
![ノーマル単細胞くん](https://user-images.githubusercontent.com/66828980/189271483-3f016be9-37df-4db4-a59e-089f9b6c52c1.png)

- 単細胞くんv2(+ OpeningAI)の[floodgateでのレート](http://wdoor.c.u-tokyo.ac.jp/shogi/view/show-player.cgi?event=LATEST&filter=floodgate&show_self_play=1&user=tansaibo_kun_v2_PLUS%2B9996535e07258a7bbfd8b132435c5962)<br>
![単細胞くん+](https://user-images.githubusercontent.com/66828980/189271490-8dced56e-a87a-4f06-a2fe-7ec3f70585ae.png)

# 今後の改良予定など
- 将来的には、状況に応じて複数の囲いを切り替えられるようにしたいと思っています。
- 今冬の電竜戦に向けて改良していく予定です。
