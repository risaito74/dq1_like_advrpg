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

# ゲーム進行用のフラグとか
default is_debug_mode = True
default is_unlock_data_center = False

# ギャラ画像の表示調整用
transform half_bottom:
    zoom 0.45
    xalign 0.7
    yalign 1.0

# 画面シェイクエフェクトの定義
transform shake:
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset 0

# =========================
# オープニング（自宅前）
# =========================
label  start:
    
    wai "…よし、なんとか外に出ることに成功したぞ…"

    wai "このまま街のあちこちを探索して、伝説のアレをアレしてやるぜ！"

    "こうして、あなたの冒険が始まった…"

# =========================
# 自宅前
# =========================
label home:

    play music "main_bgm.mp3"

    scene bg_town01 with fade

    #wai "ここは自宅前だ…"

    menu:

        wai "{color=#080}Lv：[my_lv]　MP：[my_mp]　Exp：[my_exp]　所持金：[my_yen]円{/color}\nここは自宅前だ…"

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

    "周囲を探索した…"

    # 自宅前で出現する敵：「ギャル」(100%)
    $ enemy = "gal"

    # 戻ってくる場所を設定
    $ return_place = "home"

    jump battle

# 自宅前：自宅で寝る
label rest_home:

    wai "ふう…やっぱり自分の部屋が一番じゃわい…"

    play sound "決定ボタンを押す17.mp3"

    "ワイは自宅で休憩した！\n
    MP（メンタルポイント）が全回復した！"

    # MP全回復処理
    $ my_mp = my_mp_max

    jump home

# =========================
# コンビニ前
# =========================
label convenience:

    play music "main_bgm.mp3"

    scene bg_conveni01 with fade

    menu:

        wai "{color=#080}Lv：[my_lv]　MP：[my_mp]　Exp：[my_exp]　所持金：[my_yen]円{/color}\nここはコンビニ前だ…"

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

    "周囲を探索した…"

    # コンビニ前で出現する敵：「ギャル」(50%)、「ぴえん」(50%)
    $ enemy = renpy.random.choice(["gal", "pien"])

    # 戻ってくる場所を設定
    $ return_place = "convenience"

    jump battle

# コンビニ前：コンビニに入る
label shop:

    play sound "入店チャイム.mp3"

    scene bg_shop01 with fade

    # 購入後に戻ってくる場所
    label shop_continue:

    menu:

        wai "{color=#080}Lv：[my_lv]　MP：[my_mp]　Exp：[my_exp]　所持金：[my_yen]円{/color}\nここはコンビニ店内だ…"

        "ドクターヘッツァーを買う (150円)":
            jump buy_hezza

        "たけのこ因習村を買う (200円)":
            jump buy_takenoko

        "勝ちまくりモテまくりストーンを買う！（1980円）":
            jump power_stone

        "コンビニから出る":
            play sound "入店チャイム.mp3"
            jump convenience

# コンビニ：ドクターヘッツァーを買う
label buy_hezza:

    $ price = 150

    if my_yen < price:
        "お金が足りない！"
        jump shop_continue

    $ my_yen -= price
    $ my_mp = my_mp_max
    $ my_luck += 1

    play sound "金額表示.mp3"

    "ドクターヘッツァーを飲んだ！"

    play sound "決定ボタンを押す17.mp3"

    "MP（メンタルポイント）が全回復した！"

    play sound "決定ボタンを押す17.mp3"

    "隠しパラメーター「うんのよさ」が1あがった！"

    jump shop_continue

# コンビニ：たけのこ因習村を買う
label buy_takenoko:

    $ price = 200

    if my_yen < price:
        "お金が足りない！"
        jump shop_continue

    $ my_yen -= price
    $ my_mp = my_mp_max
    $ my_luck += 2

    play sound "金額表示.mp3"

    "たけのこ因習村を食べた！"

    play sound "決定ボタンを押す17.mp3"

    "MP（メンタルポイント）が全回復した！"

    play sound "決定ボタンを押す17.mp3"

    "隠しパラメーター「うんのよさ」が2あがった！"

    jump shop_continue

# コンビニ：勝ちまくりモテまくりストーンを買う
label power_stone:

    $ price = 1980

    if my_yen < price:
        "お金が足りない！"
        jump shop_continue

    $ my_yen -= price

    play sound "金額表示.mp3"

    "ワイは勝ちまくりモテまくりストーンを手に入れた！"
    "謎のオーラがワイを包み込む…"

    $ my_luck += 50

    play sound "レベルアップ.mp3"

    "隠しパラメーター「うんのよさ」が50あがった！！"
    "なんか急に世界が優しく見えるな…"

    jump shop_continue

# =========================
# 駅前 
# =========================
label station:

    play music "main_bgm.mp3"

    scene bg_station01 with fade

    menu:

        wai "{color=#080}Lv：[my_lv]　MP：[my_mp]　Exp：[my_exp]　所持金：[my_yen]円{/color}\nここは駅前だ…"

        "周囲を調べる":
            jump search_station

        "自宅前へ行く":
            jump home

        "コンビニ前へ行く":
            jump convenience

# 駅前：周囲を調べる
label search_station:

    "周囲を探索した…"

    # 駅前で出現する敵：「メスガキ」(50%)、「ギャル」(50%)
    $ enemy = renpy.random.choice(["mesu", "gal"])

    # 戻ってくる場所を設定
    $ return_place = "station"

    jump battle

# =========================
# バトル
# =========================
label battle:

    stop music
    play sound "バーン.mp3"

    if enemy == "gal":
        $ enemy_name = "ギャル"
        $ enemy_hp = 11
        $ enemy_atk = 2
        show gal as enemy at half_bottom

    elif enemy == "pien":
        $ enemy_name = "ぴえん"
        $ enemy_hp = 14
        $ enemy_atk = 3
        show pien as enemy at half_bottom

    elif enemy == "mesu":
        $ enemy_name = "メスガキ"
        $ enemy_hp = 18
        $ enemy_atk = 4
        show mesugaki as enemy at half_bottom

    elif enemy == "chappy":
        $ enemy_name = "チャッピー"
        $ enemy_hp = 30
        $ enemy_atk = 5
        show gal as enemy at half_bottom

    "[enemy_name] があらわれた！"

    # 敵によってBGMを変える
    if enemy == "gal":
        play music "gal_battle.mp3"
    elif enemy == "pien":
        play music "pien_battle.mp3"
    elif enemy == "mesu":
        play music "mesugaki_battle.mp3"
    elif enemy == "chappy":
        play music "boss_battle.mp3"

    label battle_loop:

        # 勝利チェック
        if enemy_hp <= 0:
            jump victory

        # ゲームオーバーチェック
        if my_mp <= 0:
            jump game_over

        menu:

            "{color=#080}Lv：[my_lv]　MP：[my_mp]　Exp：[my_exp]{/color}\nどうする？"

            "たたかう":

                wai "ここを…こうじゃ！"

                play sound "重いパンチ1.mp3"

                # ダメージ値：「MP/2～MP」の乱数
                $ damage = renpy.random.randint(int(my_mp / 2),my_mp)

                $ crit = renpy.random.randint(1,100) <= my_luck * 2

                if crit:
                    $ damage *= 2
                    "かいしんのいちげき！"

                $ enemy_hp -= damage

                "[enemy_name] のHP（エッチポイント）に[damage]のダメージ！"

                if enemy_hp <= 0:
                    jump victory

                label enemy_attack:

                "[enemy_name] のこうげき！"

                # 敵ごとの一言セリフ
                if enemy == "gal":
                    $ line = renpy.random.choice([
                        "うわ、キモッ！",
                        "とりま、風呂入れし！",
                        "は？こっち見んなし！"
                    ])
                    gal "[line]"         
                elif enemy == "pien":
                    $ line = renpy.random.choice([
                        "おじさん、2万円ちょ～だい♥️",
                        "キモすぎて無理だゆ？🥺",
                        "かわいいだけじゃ、だめですか？"
                    ])
                    pie "[line]"         
                elif enemy == "mesu":
                    $ line = renpy.random.choice([
                        "ざぁ～こ、ざぁ～こ♥️",
                        "まだ泣かないでね？キャハハ♥️",
                        "よわよわじゃんｗ"
                    ])
                    mes "[line]"         

                $ my_mp -= enemy_atk

                #play sound "打撃7.mp3"
                play sound "刀で斬る2.mp3"

                # 画面シェイク演出を実行
                show layer master at shake

                "ワイのメンタルが[enemy_atk]削られた！"

                jump battle_loop

            "にげる":

                play sound "逃走.mp3"

                $ run_chance = 50 + my_luck

                if renpy.random.randint(1,100) <= run_chance:
                    hide enemy

                    "うまく逃げた！"

                    # 設定されている場所に戻る
                    jump expression return_place

                else:
                    "逃げられなかった！"

                    jump enemy_attack


# =========================
# 勝利
# =========================
label victory:

    hide enemy

    stop music
    play sound "ドンドンパフパフ.mp3"

    "[enemy_name] を倒した！"

    $ reward = renpy.random.randint(100,200)

    $ my_yen += reward

    play sound "決定ボタンを押す17.mp3"

    "[reward]円を手に入れた！"

    play sound "ジャジャーン.mp3"

    if enemy == "gal":

        "ギャルのパンティを手に入れた！"
        "ワイは「ギャルのパンティ」という謎のアイテムを使用した！"

        $ add_exp = 2

    elif enemy == "pien":

        "ストロング缶を手に入れた！"
        "ワイはストロング缶を飲んだ！\n（ワイは39歳です。お酒は20歳になってから）"

        $ add_exp = 3

    elif enemy == "mesu":

        "スポブラを手に入れた！"
        "ワイは「スポブラ」という謎のアイテムを使用した！"

        $ add_exp = 4

    $ my_exp += add_exp

    play sound "決定ボタンを押す17.mp3"

    "人生経験が[add_exp]ふえた！"

    jump level_check

# =========================
# レベルチェック
# =========================
label level_check:

    if my_exp >= my_lv * 5:

        $ my_lv += 1
        $ my_mp_max += 2
        $ my_mp = my_mp_max

        play sound "レベルアップ.mp3"

        "レベルが上がった！"

        play sound "決定ボタンを押す17.mp3"

        "MP最大値が2上がった！"

        if my_lv >= 5 and not is_unlock_data_center:
            jump unlock_data_center

    # 設定されている場所に戻る
    jump expression return_place

# =========================
# ゲームオーバー
# =========================

label game_over:

    "ワイのメンタルは完全に崩壊した…"

    "ゲームオーバー"

    return

# =========================
# データセンター解放イベント
# =========================
label unlock_data_center:

    play sound "ゴゴゴゴ.mp3"

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

# =========================
# データセンター
# =========================
label data_center:

    play music "data_center_bgm.mp3"

    scene bg_data_center01 with fade

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

# =========================
# エンディング
# =========================
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

# =========================
# ゲーム終了
# =========================
label game_end:
