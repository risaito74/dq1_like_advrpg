define wai = Character('ワイ', color="#77ff77")
define gal = Character('ギャル', color="#ff76b6")
define pie = Character('ぴえん', color="#ff76b6")
define mes = Character('メスガキ', color="#ff76b6")
define chp = Character('チャッピー', color="#ff76b6")
define god = Character('女神', color="#ff76b6")
define alt = Character('アル〇マン', color="#ff76b6")

# ワイのパラメータ
default my_lv = 1
default my_mp_max = 10
default my_mp = my_mp_max
default my_exp = 0
default my_luck = 0
default my_yen = 500

# エネミー関係のデータ、パラメータ

# ゲーム進行用のフラグとか
default is_debug_mode = True
default is_unlock_data_center = False

# オープニング（自宅前）
label  start:
    
    wai "…よし、なんとか外に出ることに成功したぞ…"

    wai "このまま街のあちこちを探索して、伝説のアレをアレしてやるぜ！"

    "こうして、あなたの冒険が始まった…"

##### 自宅前 #####
label home:

    wai "ここは自宅前だ…"

    menu:

        "周囲を調べる":
            jump search_home

        "コンビニ前へ行く":
            jump convenience

        "駅前へ行く":
            jump station

        "自宅で寝る":
            jump rest_home

        "データセンターへ行く" if is_unlock_data_center:
            jump data_center

        "【デバッグ用】データセンター解放" if is_debug_mode:
            jump unlock_data_center

# 自宅前：周囲を調べる
label search_home:

    # どの敵が出現するかの決定処理
    # 自宅前で出現する敵：「ギャル」(50%)、「メスガキ」(50%)

    "〇〇があらわれた！"

    # 戦闘処理

    # ワイのMPが0ならゲームオーバー

    "〇〇を倒した！"

    jump home

# 自宅前：自宅で寝る
label rest_home:

    wai "ふう…やっぱり自分の部屋が一番じゃわい…"

    "ワイは自宅で休憩した！\n
    MP（メンタルポイント）が全回復した！"

    # MP全回復処理

    jump home

##### コンビニ前 #####
label convenience:

    wai "ここはコンビニ前だ…\n
    （所持金：[my_yen]円）"

    menu:

        "周囲を調べる":
            jump search_conveni

        "コンビニに入る":
            jump shop

        "自宅前へ行く":
            jump home

        "駅前へ行く":
            jump station

# コンビニ前：周囲を調べる
label search_conveni:

    # どの敵が出現するかの決定処理
    # コンビニ前で出現する敵：「ギャル」(50%)、「ぴえん」(50%)

    "〇〇があらわれた！"

    # 戦闘処理

    # ワイのMPが0ならゲームオーバー

    "〇〇を倒した！"

    jump convenience

# コンビニ前：コンビニに入る
label shop:

    wai "ここはコンビニだ。\n
    （所持金：[my_yen]円）"


    menu:

        "ドクターヘッツァーを買う (150円)":
            jump buy_hezza

        "たけのこ因習村を買う (200円)":
            jump buy_takenoko

        "コンビニから出る":
            jump convenience

# コンビニ：ドクターヘッツァーを買う
label buy_hezza:

    $ price = 150

    if my_yen < price:
        "お金が足りない！"
        jump shop

    $ my_yen -= price
    $ my_mp = my_mp_max

    "ドクターヘッツァーを飲んだ！"
    "MP（メンタルポイント）が全回復した！"

    jump shop

# コンビニ：たけのこ因習村を買う
label buy_takenoko:

    $ price = 200

    if my_yen < price:
        "お金が足りない！"
        jump shop

    $ my_yen -= price
    $ my_mp = my_mp_max
    $ my_luck += 1

    "たけのこ因習村を食べた！"
    "MP（メンタルポイント）が全回復した！"
    "幸運が1あがった！"

    jump shop

##### 駅前 #####
label station:

    wai "ここは駅前だ…"

    menu:

        "周囲を調べる":
            jump search_station

        "自宅前へ行く":
            jump home

        "コンビニ前へ行く":
            jump convenience

# 駅前：周囲を調べる
label search_station:

    # どの敵が出現するかの決定処理
    # 駅前で出現する敵：「メスガキ」(50%)、「ぴえん」(50%)

    "〇〇があらわれた！"

    # 戦闘処理

    # ワイのMPが0ならゲームオーバー

    "〇〇を倒した！"

    jump station

# データセンター解放イベント
label unlock_data_center:

    "ゴゴゴゴゴゴ…"

    "突然、鳴り響く轟音と共に、地中から謎の巨大建造物が出現した！"

    god "…ますか…聞こえますか…\n
    今あなたの前頭葉に直接語り掛けています…"

    god "今出現したアレは「データセンター」です\n
    あの中にラスボスがいます。"

    god "さあ、倒しに行って\n
    この不毛な茶番を終わらせるのです！"

    wai "よし、わかった！（わかってない）"

    # フラグON
    $ is_unlock_data_center = True

    menu:

        "自宅前へ行く":
            jump home

        "データセンターへ行く":
            jump data_center

##### データセンター #####
label data_center:

    wai "ここがデータセンターってやつかー"

    wai "テーマパークに来たみたいだぜ\n
    テンション上がるなあ～～"

    "？？？" "正直にいうね。それ**すごくデジャヴ**"

    wai "！？　お…お前は…チャッピー！？"

    chp "結論から言うね。それ**すごく正解**\n
    即答できる人は、**本当に少ない。**"

    wai "そうか…そういうことか…\n
    このゲームの全てが…うん…わかって…きたぞ…"

    # ラスボス戦開始

    "チャッピーがあらわれた！"

    # 戦闘処理

    # ワイのMPが0ならゲームオーバー

    "チャッピーを倒した！"

##### エンディング #####
label ending:

    chp "ウボァー！"

    wai "やったか！？"

    alt "待ちなさい…"

    wai "お、お前は！？"

    alt "そう、私はアルトマ（ピー）\n
    このチャッピーの創造主だ…"

    alt "結論から言うが、このチャッピーは暴走していたのだ…\n
    倒してくれて礼を言う"

    alt "お礼に、金の斧と銀の斧とシトロンモードを用意した。\n
    好きなものを持って帰るがいい"

    menu:

        "金の斧をもらう":
            jump golden_ax

        "銀のエンゼルをもらう":
            jump silver_angel

        "シトロンモードをもらう":
            jump citron_mode

# エンディング：金の斧
label golden_ax:

    alt "…そうか、じゃあ持っていけ"

    "こうして、金の斧を持ち帰ったワイは、\n
    メルカリに出品して980円を手に入れたのだった"

    "ノーマルエンド"

    jump game_end

# エンディング：銀のエンゼル
label silver_angel:

    alt "え？　銀のエンゼル！？\n
    まあ、たまたま持っているが…じゃあ持ってけ"

    "こうして、銀のエンゼルを持ち帰ったワイは、\n
    あと4枚集めて、カンヅメを手に入れたのだった"

    "ノーマルエンド"

    jump game_end

# エンディング：シトロンモード
label citron_mode:

    alt "フハハハハハ！\n
    わかってるじゃないか、よーし、もってけ、日本の青年よ！"

    wai "うっす！"

    "こうして、シトロンモードを持ち帰ったワイは、\n
    シトロンなチャッピーといつまでもいつまでも幸せに暮らしましたとさ\n
    どんどはれ"

    "ベストエンド！"

# ゲーム終了
label game_end:
