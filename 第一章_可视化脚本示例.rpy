define sy = Character("SY", color="#b7d7ff")
define abiao = Character("阿表", color="#ffd7a8")
define yangwenming = Character("杨文明", color="#ffc3d8")
define feizao = Character("肥皂", color="#ffe08a")
define biecou = Character("别凑", color="#ffcc8f")
define xiaokui = Character("小葵", color="#c8f0ff")
define zhongmang = Character("种芒", color="#f5d28f")
define zhishui = Character("止水", color="#d7d1ff")
define mother = Character("母亲", color="#d9d9d9")
define shortgirl = Character("短发女生", color="#d8d8d8")

label chapter01_preview:

    scene black
    with fade

    play music "audio/bgm/ch1_theme.ogg" fadein 1.5

    centered "第一章【初遇】"

    scene bg city_car_day
    with dissolve

    "车窗外的城市一闪而过。"
    "九月的阳光被玻璃削去了一半热度，落在SY的侧脸上，像一层没什么温度的光。"

    show sy neutral at right
    with dissolve

    show mother normal at left
    with dissolve

    mother "马上就要到学校了，感觉怎么样？"

    "母亲试着把语气放轻。"
    "她看着自己的女儿，像是在面对一道很薄、却总也碰不到的墙。"

    sy "还好。"

    "回答很短。"
    "短到像是专门为了结束对话。"

    "几年前父母离婚后，SY被送进寄宿学校。"
    "从那以后，她越来越安静。"
    "她不再和人争辩，也不再主动靠近谁。"
    "更多时候，她把自己关进发呆、游戏和沉默里。"

    "母亲不是不知道。"
    "只是她太忙，也太无力。"
    "工作、应酬、补偿、安排。"
    "她能给的东西越来越多，真正陪在SY身边的时间却越来越少。"

    stop music fadeout 1.0

    scene bg campus_gate_day
    with fade

    play music "audio/bgm/campus_intro.ogg" fadein 1.5

    "樱花女子大学的大门出现在视野尽头。"
    "青灰色的墙面、金色校牌、宽阔的校门，还有门旁高高立着的两株樱花树。"

    sy "(可惜现在不是樱花开的季节。)"
    sy "(不然应该会很漂亮。)"

    scene bg dorm_day
    with dissolve

    "领完新生物料，整理完宿舍，时间已经被磨掉了大半天。"
    "母亲替她把床铺、书本和行李收拾得整整齐齐。"
    "像是想用这种细致，把这些年缺掉的陪伴稍稍补上一点。"

    show mother worried at left
    show sy neutral at right
    with dissolve

    mother "那我先走了。"
    mother "照顾好自己。周末我来接你。"

    sy "嗯。"

    hide mother
    with dissolve

    "门关上以后，宿舍一下子安静下来。"
    "SY坐在椅子上，盯着面前那排刚摆好的书发呆。"

    "她从小就喜欢发呆。"
    "不是因为无聊。"
    "只是只有在那种精神抽离的瞬间，她才觉得自己是自由的。"

    "她发呆太专注。"
    "专注到有人推门进来，她都没有立刻察觉。"

    play sound "audio/sfx/door_open.ogg"

    show abiao smile at left
    with dissolve

    abiao "同学？"

    "肩膀被轻轻拍了一下，SY这才猛地回神。"
    "她转过头时，眼神里还残留着没来得及收起的惊惶。"

    show sy surprised at right
    with dissolve

    abiao "你好同学，我叫阿表，是你的新室友。"

    "对方扎着可爱的双马尾，皮肤白得晃眼，笑起来毫不设防。"
    "她像是完全没有读懂SY身上的冷意，又或者读懂了，也并不在意。"

    show sy neutral at right

    sy "我叫SY。"

    abiao "那以后请多关照啦。"

    "SY点了点头。"
    "这场相遇简短得像一滴水落进杯子里。"
    "没有波澜，只留下了一个名字。"

    scene bg plaza_sunset
    with fade

    play music "audio/bgm/plaza_evening.ogg" fadein 1.5

    "傍晚，新生们被集中到学校广场。"
    "空气里混着汗味、夕阳和一点刚入学的人才会有的兴奋。"

    show sy neutral at center
    with dissolve

    "只有SY站得笔直。"
    "她像一名误入人群的士兵，和四周的热闹格格不入。"

    show abiao talk at left
    with dissolve

    "阿表已经和另外两个室友聊了起来。"
    "她很快就能融进任何气氛里。"
    "而SY则像一块被刻意留白的区域，谁靠近，谁都会先停一下。"

    hide abiao
    with dissolve

    "就在这时，广场上的喧闹被麦克风放大的声音压了下去。"

    "军训说明、注意事项、各种流程安排依次被念出来。"
    "SY听着，却像没听。"

    play sound "audio/sfx/mic_on.ogg"

    scene bg plaza_stage_evening
    with dissolve

    show yangwenming formal at center
    with dissolve

    yangwenming "大家好，我是杨文明，是樱花女子大学学生会的会长。"

    "SY抬了头。"
    "那是她今天第一次真正把注意力从自己的世界里抽出来。"

    "台上的女生穿着正装，声音甜，却不软。"
    "她有一张很容易让人联想到果汁和甜点的脸。"
    "可再仔细看，又会发现那双眼睛过于笃定，甚至带着一点不容忽视的侵略性。"

    sy "(真是有趣的长相。)"

    scene bg training_field_day
    with fade

    play music "audio/bgm/training_loop.ogg" fadein 1.0

    "军训的日子很快过去。"
    "SY被晒黑了一点，脸颊也被晒出浅红的痕迹。"
    "可比起大部分人，她吃的苦并不算多。"
    "她站军姿很稳，动作也标准。"

    show abiao tired at left
    show sy neutral at right
    with dissolve

    abiao "我真的不行了……"
    abiao "为什么你一点都不像刚被太阳烤过的人？"

    sy "你已经很像了。"

    abiao "……这算安慰吗？"

    "阿表解散后常常整个人挂到SY背上。"
    "久而久之，两人也比刚见面时熟络了不少。"

    scene bg hall_outside_evening
    with fade

    play music "audio/bgm/festival_prelude.ogg" fadein 1.5

    "军训最后一天的晚上，学校办了迎新晚会。"
    "阿表一路都很兴奋。"

    show abiao excited at left
    show sy neutral at right
    with dissolve

    abiao "SY！你说我进话剧社怎么样？"
    abiao "辩论社也不错吧？还是说cos社更适合我？"

    sy "都好。"

    abiao "你果然还是这句。"

    scene bg hall_inside_night
    with dissolve

    "宴会厅里人很多。"
    "灯光、噪音、节目、欢呼。"
    "一切都很大学。"

    "阿表看得津津有味，SY却始终有点游离。"
    "她低头刷了一会手机，再抬头时，舞台上已经换了节目。"

    scene bg stage_glow
    with fade

    play music "audio/bgm/slow_motion_theme.ogg" fadein 1.5

    "一束光打了下来。"
    "光里站着一个金发女生。"

    "原本只是随意一瞥。"
    "可视线对上的那一秒，SY像是被某种极细微、却极准确的电流击中了。"

    show sy stunned at center
    with dissolve

    "她忽然不想移开眼。"
    "于是就那样看了下去。"
    "看她的身形、看她的舞步、看她在灯下闪着光的头发。"
    "也看她像什么都不知道一样，理所当然地占据了整块舞台。"

    sy "(这个人……到底是谁。)"

    scene bg hall_inside_night
    with dissolve

    "节目结束得很快。"
    "可SY的视线还停在刚才那片空出来的地方。"

    show abiao curious at left
    show sy tense at right
    with dissolve

    sy "刚刚那首歌，叫什么？"

    abiao "啊？我没注意诶。"

    "SY心里一沉。"

    shortgirl "slow motion。"

    "声音来自SY另一边。"
    "她愣了半拍，才反应过来这是在回答自己。"

    sy "谢……"

    play sound "audio/sfx/light_bump.ogg"

    "她一转头，正好撞上那名短发女生探过来的半个脑袋。"

    shortgirl "抱歉抱歉。"
    sy "不，是我没看好。"

    "对方摆了摆手，很快又把注意力收回了舞台。"
    "只留下银色耳钉闪过的一线光，和嘴角边一颗淡淡的痣。"

    scene bg dorm_night
    with fade

    play music "audio/bgm/night_loop.ogg" fadein 1.5

    "回到宿舍后，晚会的喧闹终于散去。"
    "可SY的大脑没有安静下来。"

    "她戴上耳机，一遍又一遍地听那首《slow motion》。"
    "像是在确认今晚真的发生过什么。"
    "又像是在借着这首歌，把那个金发背影牢牢记住。"

    show sy alone at center
    with dissolve

    sy "还能再见到你吗。"

    stop music fadeout 2.0

    return

label chapter02_preview:

    scene black
    with fade

    play music "audio/bgm/ch2_theme.ogg" fadein 1.5

    centered "第二章【狙击】"

    scene bg campus_path_day
    with dissolve

    "迎新晚会之后，SY开始有意在校园里乱逛。"
    "她明知道这行为毫无根据，却还是忍不住想在人群里重新找到那个金发身影。"
    "几天过去，毫无线索。"
    "她终于决定放弃。"

    scene bg cafeteria_road_day
    with fade

    show abiao smile at left
    show sy neutral at right
    with dissolve

    abiao "今天换个食堂吧？"
    abiao "我想吃芝士紫菜包饭。"

    "那家食堂离纳新街很近。"
    "SY原本不太想去，但想想开学也有几天了，摊位大概早散了。"

    sy "行。"

    "两人刚走到食堂外，SY就被人轻轻拍了拍肩。"

    play sound "audio/sfx/tap.ogg"

    show feizao grin at center
    with dissolve

    feizao "嘿，同学。"

    "站在她们面前的是个短发女生。"
    "金色短发、利落眉眼，还有一种近乎少年的帅气。"

    feizao "我看你个子高，挺适合打篮球。"
    feizao "我们队最近正缺人，要不要来试试？"

    sy "我没打过。"

    feizao "那更好教啊。"
    feizao "你这个身高，往篮下一站，光伸手就够吓人了。"

    "对方越说越起劲，像是生怕眼前这个高个新生下一秒就跑了。"

    feizao "这样，我给你张海报。"
    feizao "下午四点半，球馆训练。"
    feizao "你来看看也行。"

    "她把一张被揉得有点发皱的海报塞到SY手里，转身走了几步，又猛地回头。"

    feizao "对了，我叫肥皂。篮球队队长。"
    feizao "你一定要来哦！"

    hide feizao
    with dissolve

    abiao "这不是挺好吗？"
    abiao "来大学总得进个社团吧。"
    abiao "你总不能一直窝在宿舍打游戏。"

    sy "我会考虑。"

    "她低头看着那张设计得相当随便的海报，忍不住想。"
    sy "(这宣传也太不走心了。)"
    sy "(难怪招不到人。)"

    scene bg gym_interior_day
    with fade

    play music "audio/bgm/basketball_day.ogg" fadein 1.5

    "下午四点，SY还是换上运动服去了球馆。"
    "刚进门，她就听见篮球连续撞击地板的声音。"

    show biecou dribble at center
    with dissolve

    "视线尽头，一个黑发小个子正利落地上篮。"
    "球落进框里的瞬间，对方转身去捡球，左脸上的那颗痣也跟着闯进SY的记忆。"

    sy "(是她。)"
    sy "(迎新晚会坐在我旁边的那个短发女生。)"

    biecou "啊，你是那天在宴会厅问《slow motion》的人。"
    biecou "你也是来打球的吧？"

    show sy awkward at right
    with dissolve

    sy "……听说下午有训练，就来看看。"

    biecou "是肥皂欧尼拉你来的吧？"
    biecou "她最喜欢到处物色新人了。"

    "两人在场边坐了一会儿，训练的人慢慢到齐。"
    "最后进门的果然是肥皂。"

    show feizao grin at left
    with dissolve

    feizao "你真来了。"

    "自我介绍开始后，SY才正式知道黑发小个子的名字。"

    biecou "我叫别凑。"

    sy "(这名字和本人也太不搭了。)"

    "接下来的一整个下午，SY学得出奇地快。"
    "运球、传球、三步上篮，几乎一上手就能抓住感觉。"

    feizao "……你这不是挺会的嘛。"

    "肥皂原本只想给她安排个靠身高吃饭的位置。"
    "现在却开始认真考虑，要不要直接把她往主力培养。"

    scene bg gym_exit_sunset
    with dissolve

    "训练结束后，SY擦着汗，顺手递了几张湿巾给别凑。"

    biecou "谢啦。"
    biecou "你借我纸，我请你喝绿豆沙，怎么样？"

    sy "绿豆沙是什么？"

    biecou "……你连这个都没喝过？"
    biecou "走，我请你。"

    scene bg drink_shop_evening
    with fade

    "冰凉的绿豆沙顺着喉咙一路滑下去。"
    "刚训练完时那股燥热，被一点点压了下去。"

    sy "嗯，好喝。"

    show biecou smile at left
    with dissolve

    "别凑眯起眼笑了。"
    "笑起来的时候，她左脸那颗痣反而显得格外生动。"

    "两人加了联系方式，各自回宿舍。"
    "SY忽然觉得，自己在大学里，好像终于开始和某些人真正产生联系了。"

    scene bg backstage_dark
    with fade

    play music "audio/bgm/stage_glamour.ogg" fadein 1.5

    "几天后，阿表因为感冒，把一个学生会的督场任务丢给了SY。"
    "SY穿着借来的黑色西装，被迫站在舞台边发呆。"

    "会场灯光暗下来以后，她反而自在了一点。"
    "直到主持人念出下一个节目。"

    "MOSA 舞团，《Feel Special》。"

    scene bg stage_blackout
    with dissolve

    "舞台完全暗下。"
    "紧接着，一束灯从正中打亮。"

    scene bg stage_glow
    with fade

    "长长的金发在灯下发亮。"
    "那个人站在最亮的地方，像是比光还要更先一步抓住人的视线。"

    "这一次，SY终于离她足够近。"
    "近到足以看清她的笑、她的眼神，和她举手投足间那种几乎无声的攻击性。"

    sy "(就是她。)"

    "节目结束后，金发女生和队友一起朝后台出口走来。"
    "SY站在角落，一动不敢动。"

    "可对方走到一半，忽然停下，低头捡起了什么。"
    "再抬头时，那双眼睛直直地落在了SY身上。"

    show zhongmang at center
    with dissolve

    zhongmang "这是你掉的吧？"
    zhongmang "下次要小心一点。"

    "她递过来的是SY的饭卡。"
    "直到这时，SY才发现西装裤的口袋裂了个口子。"

    sy "……谢谢。"

    "取回饭卡时，两人的指尖轻轻碰到一起。"
    "冰凉、柔滑，一触即分。"

    "可等那人走远以后，SY还是站在原地，很久都没动。"

    stop music fadeout 2.0

    return

label chapter03_preview:

    scene black
    with fade

    play music "audio/bgm/ch3_theme.ogg" fadein 1.5

    centered "第三章【线索】"

    scene bg dorm_morning
    with dissolve

    show abiao sick at left
    show sy lying at right
    with dissolve

    abiao "SY，不要再生我的气啦。"
    abiao "同情一下病人好不好？"

    "阿表把纸巾团成一团塞在鼻孔里，可怜兮兮地仰头看着上铺。"
    "SY躺在床上，一句话也不说。"

    "前一天晚上回来以后，她只给阿表看了那个破掉的裤兜，就把自己卷进沉默里。"

    sy "(还是没能知道你的名字。)"

    scene bg basketball_court_day
    with fade

    play music "audio/bgm/daily_training.ogg" fadein 1.5

    "正式进队以后，SY保持着规律训练。"
    "而别凑，也渐渐成了除了阿表之外，陪她最久的人。"

    show sy neutral at right
    show biecou talk at left
    with dissolve

    "这天训练结束，两人照旧去食堂喝绿豆沙。"
    "别凑边走边讲新听来的笑话，讲到一半，迎面撞上了一个端着餐盘的女生。"

    play sound "audio/sfx/tray_drop.ogg"

    "金属餐盘落地，发出一连串刺耳声响。"

    show xiaokui startled at center
    with dissolve

    "白色连衣裙上溅了污渍。"
    "别凑整个人当场僵住。"

    biecou "对不起对不起对不起。"
    biecou "我赔你一件行不行？"

    "对方没有立刻说话，只是低头看着裙摆。"
    "SY走过去，把湿巾递给她。"

    sy "先擦一下吧。"

    xiaokui "……谢谢。"

    "女生抬头的瞬间，别凑像被雷劈了一下。"
    "肤色白净、五官精巧、眼神雾蒙蒙的，简直像从画里掉下来的人。"

    biecou "(这不是仙女吗。)"

    play sound "audio/sfx/footstep_soft.ogg"

    show zhishui cool at left
    with dissolve

    zhishui "小葵，怎么了？"

    "又有两个人走近。"
    "其中一个是戴圆框眼镜的女生。"
    "而另一个，正是那个让SY惦记了许久的金发身影。"

    "世界有时候很大。"
    "有时候又小得过分。"

    "SY一句话都说不出来。"
    "远处那个人却像是认出了她，嘴角很轻地动了一下。"

    xiaokui "没事，刚才不小心撞到了。"

    zhishui "小朋友都不问问价格的吗？"
    zhishui "小葵的衣服可不便宜。"

    biecou "是我撞的。"
    biecou "我赔。"

    "她说得硬气，气势却明显没有平时足。"
    "还没等局面继续僵下去，小葵就先一步拉住了止水。"

    xiaokui "算了。"
    xiaokui "衣服脏了，再换一件就是。"

    "几人离开前，那个金发女生又淡淡扫了SY一眼。"
    "轻、短，却精准得像一根针。"

    hide xiaokui
    hide zhishui
    with dissolve

    biecou "阿西，今天真倒霉。"

    sy "我倒觉得……更倒霉的是她。"

    biecou "不行。"
    biecou "这事不能就这么算了。"
    biecou "我要找到她，赔她。"

    "说完这话，她连绿豆沙都顾不上喝完，转头就开始筹划下一步。"

    scene bg dorm_corridor_evening
    with fade

    "第二天，别凑抱着一大袋拼图和模型找上SY。"

    sy "这就是你说的赔偿？"

    biecou "我都打听好了。"
    biecou "她叫小葵，喜欢拼图和模型。"
    biecou "我买的可都是高难度款。"

    sy "……为什么我要陪你一起去？"

    biecou "因为你是我在这个学校最好的朋友啊。"
    biecou "而且那个眼镜女看起来太凶了。"

    scene bg senior_dorm_door
    with dissolve

    play sound "audio/sfx/knock.ogg"

    xiaokui "请进。"

    scene bg senior_dorm_inside
    with dissolve

    show xiaokui calm at center
    show biecou stiff at left
    show sy neutral at right
    with dissolve

    "寝室里只有小葵一个人。"
    "这让别凑明显松了口气。"

    biecou "中午那件事真的很抱歉。"
    biecou "我听说你喜欢拼图，就……带了点过来。"

    xiaokui "谢谢。"

    "她把袋子接过去，神情依旧温和。"
    "可别凑却像突然被什么吓到似的，话没说完就拉着SY飞快撤退。"

    scene bg dorm_hallway_evening
    with dissolve

    sy "你跑什么？"

    biecou "我还以为那个眼镜女会在。"

    "SY无言地看着她。"
    "原来这人真正怕的是止水。"

    "就在两人说话的时候，一阵极淡的香气从身边掠过去。"
    "SY下意识偏头，正好撞上一双水雾一样的眼睛。"

    "视线只接触了不到一秒。"
    "可那股海盐和柠檬混在一起的气息，已经留在了她呼吸里。"

    sy "(像海风。)"

    scene bg campus_road_evening
    with fade

    "走出宿舍楼后，别凑还在旁边叽叽喳喳。"
    "可SY已经没太听见了。"
    "她脑子里只剩下零散的线索。"

    "金色的光。"
    "冰凉的触感。"
    "海风一样的味道。"

    "这些碎片拼在一起，终于让她意识到，自己正在以一种从未有过的方式，记住另一个人。"

    biecou "喂！SY！"

    sy "啊？"

    biecou "我说，我想追小葵。"

    "SY停住脚步。"
    "这句话比她刚才脑子里所有混乱的线索加起来都更有冲击力。"

    sy "……为什么？"

    biecou "哪有那么多为什么。"
    biecou "我就是想追。"

    stop music fadeout 2.0

    return

label chapter04_preview:

    scene black
    with fade

    play music "audio/bgm/ch4_theme.ogg" fadein 1.5

    centered "第四章【咒语】"

    scene bg dorm_corridor_morning
    with dissolve

    "别凑说要追小葵之后，整整一个月都没有消停。"
    "她不知道从哪里弄来了小葵的课表，几乎把自己活成了一张会移动的偶遇计划表。"

    scene bg senior_dorm_morning
    with fade

    show biecou at left
    show sy neutral at right
    with dissolve

    "有时候她躲在宿舍楼对面的灌木后面。"
    "有时候她拎着早餐在楼下假装路过。"
    "再不然，就抱着水瓶蹲在网球场边，装作自己只是恰好经过。"

    biecou "你说这次够自然吗？"
    sy "不像自然。"
    sy "像埋伏。"

    "起初，小葵还会礼貌地点头。"
    "后来她开始学会视而不见。"
    "再后来，她干脆连网球都不去打了。"

    biecou "我有这么可怕吗？"
    sy "有一点。"

    "在SY的劝说下，别凑终于决定暂时收敛。"

    scene bg basketball_arena_day
    with fade

    play music "audio/bgm/tournament_open.ogg" fadein 1.5

    "十月底，全国大学生篮球赛开打。"
    "樱花女大的首场比赛就在本校体育馆举行。"
    "对于整个篮球队来说，这是入秋以来最重要的一天。"

    show feizao grin at left
    show sy neutral at center
    show biecou at right
    with dissolve

    feizao "今天都给我稳住。"
    feizao "先把第一场拿下来。"

    biecou "放心吧队长。"
    biecou "我今天状态特别好。"

    sy "(但你昨天晚上紧张到三点还没睡。)"

    scene bg arena_stands_day
    with dissolve

    show xiaokui calm at left
    show zhishui cool at center
    show zhongmang at right
    with dissolve

    "另一边，种芒以散步为名，把止水和小葵一路带进了体育馆。"

    zhishui "你不是最不爱看球赛吗？"

    zhongmang "偶尔也会想看看热闹。"

    "止水和小葵坐下后开始闲聊。"
    "种芒却从头到尾都没怎么接话。"
    "她的视线越过嘈杂的人群，轻易就锁定了场中央那个正在热身的高个新生。"

    zhongmang "(找到你了。)"

    scene bg basketball_court_match
    with fade

    play music "audio/bgm/match_drive.ogg" fadein 1.0

    "哨声一响，比赛开始。"
    "SY和别凑的配合比训练时还要默契。"
    "挡拆、快攻、突分，第一节结束时，樱花队已经把比分拉开。"

    show sy determined at center
    show biecou dribble at left
    with dissolve

    "看台上的欢呼一浪高过一浪。"
    "有人在喊SY的名字，也有人举起手机拍下她上篮时的瞬间。"

    scene bg arena_stands_day
    with dissolve

    show zhongmang at center
    with dissolve

    zhongmang "人气这么高啊。"

    "她明明在笑。"
    "可那笑意像薄雾，漂亮，却并不温柔。"

    scene bg basketball_court_match
    with fade

    "第二节开始后，对手突然换了打法。"
    "她们不再只盯球，而是开始盯人。"
    "更准确地说，是开始死盯SY。"

    "绊脚、挤撞、暗拐、落地时故意抢位。"
    "那些动作刚好都踩在裁判最难抓的边缘。"

    show sy strained at center
    with dissolve

    "SY还能撑住。"
    "可她撑得越来越难。"

    feizao "裁判，这已经不是正常防守了！"

    "抗议并没有立刻换来结果。"
    "直到下一次突破时，SY在边线附近被人恶意撞翻。"

    play sound "audio/sfx/whistle_long.ogg"

    "全场安静了一秒。"
    "紧接着，嘘声和怒骂一起炸开。"

    show biecou angry at left
    show sy down at center
    with dissolve

    biecou "你手不干净是吧？"

    "别凑冲上去揪住对方领口，差点连自己的黄牌一起领回来。"
    "而SY被扶起来时，右脚已经明显站不稳了。"

    scene bg bench_area_day
    with dissolve

    "队医确认只是扭伤。"
    "可在这种节骨眼上，任何伤都足够致命。"

    show feizao serious at center
    with dissolve

    "就在场边一片混乱的时候，肥皂沉默地套上了球衣。"
    "自从旧伤留下以后，她很少再亲自上场。"
    "可这一次，她没有再犹豫。"

    feizao "(抱歉，杨文明。)"

    scene bg basketball_court_match
    with fade

    "重新开球后，肥皂像把压了很久的锋刃。"
    "她的节奏比SY更凶，爆发力也更直接。"
    "一个急停晃开防守，下一秒，三分空心入网。"

    play sound "audio/sfx/crowd_cheer.ogg"

    "看台上的声浪再次被点燃。"
    "那一球像一记强心针，硬生生把樱花队从乱局里拽了回来。"

    scene bg infirmary_day
    with fade

    play music "audio/bgm/infirmary_soft.ogg" fadein 1.5

    "而SY已经被送去了校医院。"
    "止痛片让她有些发困。"
    "可她手机玩到一半，还是本能地抬起了头。"

    "那股气味又出现了。"

    show zhongmang at center
    with dissolve

    "种芒把牛奶和零食放到床头，自己拉了把椅子坐下。"
    "她什么都没急着说，只是托着下巴，安静地看着SY。"

    sy "……"

    zhongmang "SY。"
    zhongmang "还记得我吗？"

    "她的声音很轻，像贴着耳骨滑过去。"
    "SY忽然觉得，病房里的空气都被这句话压窄了。"

    sy "记得。"
    sy "只是……我还不知道你的名字。"

    zhongmang "想知道？"

    "SY点头。"

    zhongmang "我叫种芒。"
    zhongmang "现在记住了吗？"

    sy "记住了。"

    "种芒像是被这个回答取悦了。"
    "她站起身时，裙摆在床边扫出一点很轻的弧度。"

    zhongmang "那就好。"
    zhongmang "别再把自己弄伤了。"

    hide zhongmang
    with dissolve

    "她来得突然，走得也突然。"
    "可她一离开，整间病房都像被她带走了什么。"

    scene bg infirmary_night
    with fade

    "晚一点，别凑和肥皂来报喜，说比赛最后还是赢了。"
    "别凑边说边比划，恨不得把自己今天每一次抢断都重新演一遍。"
    "她成功把SY逗笑了。"

    scene bg infirmary_night
    with dissolve

    "再晚一点，值班大爷送来一份盒饭。"
    "饭盒上贴着一张粉色便签。"

    sy "多吃饭，长得快……"

    "字很可爱。"
    "可爱得不像别凑，也不像肥皂，更不像阿表。"

    "SY盯着那张便签看了很久，才慢慢念出那个名字。"

    sy "种芒。"

    "这两个字从唇齿间滑出来时，像某种真正生效的咒语。"

    stop music fadeout 2.0

    return

label chapter05_preview:

    scene black
    with fade

    play music "audio/bgm/ch5_theme.ogg" fadein 1.5

    centered "第五章【草木】"

    scene bg dream_white
    with dissolve

    "白茫茫的梦里，没有门，也没有出口。"
    "只有一种湿润又甜得过分的声音，一遍遍喊她的名字。"

    zhongmang "SY。"

    "SY猛地惊醒。"

    scene bg dorm_morning
    with fade

    show sy startled at center
    with dissolve

    "自从种芒来过病房以后，她已经连续做了好几天这种梦。"
    "而那几盒牛奶，也被她喝得干干净净。"

    sy "(难道她真的会下蛊。)"

    "不过伤倒是好得很快。"
    "一周不到，SY就重新回到了训练里。"

    scene bg barbecue_night
    with fade

    play music "audio/bgm/team_dinner.ogg" fadein 1.5

    "为了给队伍提气，也为了庆祝SY归队，肥皂请全队去吃烤肉。"
    "她嘴上说只是普通聚餐，实际上一看就是偷偷动了点队费。"

    show feizao grin at left
    show biecou smile at center
    show sy neutral at right
    with dissolve

    feizao "都给我多吃点。"
    feizao "输了球可以复盘，饿着肚子不行。"

    biecou "队长英明。"

    "那一晚，SY第一次真切地感觉到，篮球队不只是一群一起打球的人。"
    "它更像一个会吵闹、会偏心、但也会在关键时刻把你接住的小团体。"

    scene bg equipment_room_day
    with fade

    stop music fadeout 1.0
    play music "audio/bgm/tension_low.ogg" fadein 1.0

    "几天后的一次午训结束，SY回体育馆拿落下的水杯。"
    "路过器械室时，她听见里面有人说话。"

    yangwenming "听说你这次比赛打得不错。"

    feizao "杨文明……我想跟你谈谈。"

    "SY本来不想偷听。"
    "可那两个人的声音实在太清楚。"

    yangwenming "如果还是那件事，就不用说了。"
    yangwenming "我已经拒绝过你。"

    feizao "我答应你的事，我会做到。"
    feizao "再给我一点时间。"

    yangwenming "你答应我的，已经不止这一件了。"
    yangwenming "包括不上场。"

    "沉默像绷紧的弦。"
    "没过多久，脚步声朝门口走来，SY立刻躲进了旁边的洗手间。"

    scene bg corridor_day
    with dissolve

    "等杨文明离开以后，她才慢慢吐出一口气。"

    sy "(她们两个……到底是什么关系。)"

    scene bg dorm_corridor_evening
    with fade

    play music "audio/bgm/light_comedy.ogg" fadein 1.2

    show biecou pleading at left
    show sy neutral at right
    with dissolve

    biecou "SY，帮我个忙。"
    biecou "陪我去和小葵吃饭。"

    sy "她不是不肯单独和你出去吗？"

    biecou "所以我才需要你。"
    biecou "你在旁边，我就没那么像变态。"

    sy "……你对自己的定位还挺准确。"

    scene bg barbecue_restaurant_night
    with fade

    play music "audio/bgm/awkward_dinner.ogg" fadein 1.0

    "两人提前到了烤肉店。"
    "可等她们推门进去时，桌边已经坐了三个人。"

    show xiaokui calm at left
    show zhishui cool at center
    show zhongmang at right
    with dissolve

    "小葵。止水。还有种芒。"

    biecou "……你只说不想单独见我。"
    biecou "没说你会带一整队人。"

    zhishui "你不也带了SY？"

    "别凑被堵得哑口无言。"
    "而真正最想立刻逃跑的人，其实是SY。"

    scene bg barbecue_restaurant_night
    with dissolve

    "点单时，止水像打仗一样在菜单上画勾。"
    "种芒则顺手把菜单递给了SY。"

    zhongmang "我们点好了。"
    zhongmang "你们看看，还要不要加什么？"

    "桌子是长方形的。"
    "这让SY和种芒之间的距离，比病房那次还要近。"

    sy "(冷静。)"
    sy "(我是来陪别凑吃饭的。)"

    "肉上桌以后，尴尬稍微散了一点。"
    "止水负责吃。"
    "别凑负责往小葵盘子里夹肉。"
    "而小葵吃得很慢，慢得像在替所有人拖延什么。"

    "SY其实也没吃进去多少。"
    "她只是在低头时，偶尔会用余光看种芒。"
    "看她慢条斯理地咀嚼，看她垂眼时柔和下来的轮廓。"

    sy "(有点像松鼠。)"

    "想到这里，SY差点笑出声，只好低头喝水掩饰。"

    scene bg barbecue_restaurant_night
    with dissolve

    "最后，真正打破僵局的人是小葵。"

    xiaokui "我已经提前结过账了。"

    "说完，她起身就走。"
    "别凑愣了一秒，立刻追了出去。"

    hide xiaokui
    hide biecou
    with dissolve

    "没过多久，止水也接了个电话离开。"
    "于是五个人的饭局，转眼只剩下两个人。"

    hide zhishui
    with dissolve

    scene bg street_night
    with fade

    "SY和种芒沿着街边慢慢往学校走。"
    "谁也没说话。"
    "可沉默并不尴尬，反而像一条被默契拉出来的细线。"

    play sound "audio/sfx/stumble.ogg"

    "走到路口时，种芒忽然被翘起的地砖绊了一下。"

    show zhongmang at center
    show sy surprised at right
    with dissolve

    sy "小心。"

    "SY扶住她，才发现她掌心擦破了皮，膝盖也蹭红了一块。"

    scene bg pharmacy_night
    with dissolve

    "几分钟后，SY拎着药袋跑回原地。"
    "棉签、药水、创可贴。"
    "还有一盒她顺手拿上的柠檬薄荷糖。"

    scene bg street_night
    with fade

    show zhongmang at center
    show sy kneel at right
    with dissolve

    "她蹲下来替种芒处理伤口。"
    "种芒的手很白，也很凉。"
    "指尖在疼的时候会微微蜷起，像在克制什么。"

    zhongmang "你一直都这么会照顾人吗？"

    sy "没有。"
    sy "只是今天刚好轮到你。"

    "种芒笑了笑，没再接这句话。"

    scene bg taxi_night
    with dissolve

    "之后，SY拦了辆出租。"
    "她把种芒送到学校侧门，又把自己的外套披到她肩上。"

    zhongmang "你不冷吗？"

    sy "还好。"

    "这次轮到种芒看着她。"
    "看得很慢，也很仔细。"

    scene bg senior_dorm_night
    with fade

    show zhongmang at left
    show sy neutral at right
    with dissolve

    sy "要我送你上去吗？"

    zhongmang "不用。"
    zhongmang "谢谢你，SY。"

    "她转身走了几步，又想起肩上还披着那件外套。"

    zhongmang "这个呢？"

    sy "下次再还我。"

    "她说完就后悔了。"
    "因为这句话听起来，简直像在给自己制造下一次见面的理由。"

    scene bg zhongmang_room_night
    with fade

    play music "audio/bgm/quiet_thoughts.ogg" fadein 1.0

    "回到宿舍后，种芒坐在椅子上休息了很久。"
    "然后，她把那件黑色外套拎起来，轻轻凑到鼻尖。"

    zhongmang "……是草木的味道。"

    "不像花，也不像果。"
    "更像雨后树皮、泥土和风一起留下的气息。"

    stop music fadeout 2.0

    return

label chapter06_preview:

    scene black
    with fade

    play music "audio/bgm/ch6_theme.ogg" fadein 1.5

    centered "第六章【心意】"

    scene bg xiaokui_room_day
    with dissolve

    "别凑最近的存在感，高得让小葵想装看不见都难。"
    "她会在宿舍楼下出现，在食堂里出现，在去上课的路上出现。"
    "有时候还会送来一些过于用力的礼物。"

    xiaokui "(纯白地狱拼图，到底是谁会把这个当赔礼。)"

    "可奇怪的是，她并没有真的讨厌别凑。"
    "甚至偶尔会觉得，那个人莽撞得有点可爱。"

    scene bg flashback_window
    with fade

    "小葵从小生活优渥。"
    "父亲是医生，母亲是律师，哥哥和父母把她护得很好。"
    "她学了很多年芭蕾，也因此比旁人更敏感、更容易受伤。"

    "真正让她变得警惕的，是高中那段并不愉快的时光。"

    scene bg flashback_alley
    with dissolve

    "语言不通，环境陌生。"
    "她曾在放学路上被一群女生堵进窄巷，连求救都发不出声音。"

    play sound "audio/sfx/motor_stop.ogg"

    show zhishui cool at center
    with dissolve

    "救她的人是止水。"
    "那个时候的止水骑着机车，一身黑，像突然闯进现实的坏脾气英雄。"

    zhishui "欺负人之前，最好先掂量一下自己。"

    scene bg flashback_home
    with fade

    show zhongmang at left
    show zhishui cool at center
    show xiaokui calm at right
    with dissolve

    "那天晚上，小葵第一次见到种芒。"
    "也是从那天开始，她慢慢拥有了真正意义上的朋友。"

    "后来她谈过一次恋爱。"
    "开始很漂亮，结束得却很狼狈。"
    "那之后，小葵就更难轻易相信谁了。"

    scene bg barbecue_restaurant_night
    with fade

    "所以当她意识到别凑不是在玩笑，而是真的在追她时，她第一反应不是生气。"
    "而是慌张。"

    "她本来想在那顿烤肉时好好说清楚。"
    "可准备了很久的话，最后只变成了一句提前结账。"

    scene bg milktea_shop_night
    with dissolve

    "从店里出来的时候，别凑还站在不远处。"
    "帽子压得很低，像一只被雨打湿了耳朵的小狗。"

    show xiaokui calm at left
    show biecou at right
    with dissolve

    xiaokui "你追这么远，怎么不叫我？"

    biecou "我怕你不想见我。"
    biecou "但又怕你一个人出事。"

    "小葵一下子说不出话。"
    "她看着别凑那双亮得过分的眼睛，忽然有点不知道该拿这个人怎么办。"

    xiaokui "那你饿不饿？"
    xiaokui "要不要喝奶茶。"

    biecou "我要和你一样的。"

    scene bg milktea_shop_night
    with dissolve

    "小葵又买了一杯抹茶奶绿。"
    "别凑接过以后，像拿到了什么珍贵奖章一样，喝得认真又郑重。"

    biecou "好喝。"
    biecou "不愧是你喜欢的。"

    "那一瞬间，小葵忽然笑了。"
    "刚才在心里积压的烦躁和顾虑，也一起散掉了。"

    xiaokui "(真是个……蠢得可爱的人。)"

    stop music fadeout 2.0

    return

label chapter07_preview:

    scene black
    with fade

    play music "audio/bgm/ch7_theme.ogg" fadein 1.5

    centered "第七章【假酒】"

    scene bg restaurant_day
    with dissolve

    "从那之后，小葵和别凑之间像是悄悄达成了某种停战协议。"
    "小葵不再刻意躲她。"
    "别凑也不再像之前那样高频率地刷存在感。"

    "只是她们偶尔约饭时，依旧会把约会吃成群体活动。"

    show zhishui cool at left
    show biecou at center
    show sy neutral at right
    with dissolve

    zhishui "你也是打篮球的，怎么天天还带保镖？"

    biecou "那您不是也每次都来蹭饭吗，学姐？"

    "止水和别凑一见面就拌嘴。"
    "小葵头疼。"
    "种芒却看得津津有味。"

    scene bg dinner_table
    with fade

    show zhongmang at center
    with dissolve

    "她尤其喜欢看SY坐在对面时那副努力装镇定的样子。"
    "上次药店之后，种芒开始记住更多和SY有关的细节。"
    "比如她的掌心很暖，动作很稳。"
    "再比如，她身上总带着一点清爽的草木气息。"

    zhongmang "(真奇怪。)"
    zhongmang "(怎么会有人闻起来像刚下过雨的树林。)"

    scene bg training_field_morning
    with fade

    play music "audio/bgm/training_hard.ogg" fadein 1.0

    "另一边，全国赛还在继续。"
    "为了给两个新人补足对抗和体能，肥皂把训练强度直接往上提了一个档。"

    show feizao serious at left
    show sy tired at center
    show biecou exhausted at right
    with dissolve

    feizao "硬拉做完去蛙跳。"
    feizao "别装死。"

    biecou "队长你没有心。"
    biecou "我要退队。"

    sy "你昨天也这么说。"

    "训练结束时，SY累得回寝室倒头就睡。"

    scene bg dorm_evening
    with fade

    show abiao at left
    show sy sleepy at right
    with dissolve

    "她是被阿表手机外放的视频声吵醒的。"

    sy "你在看什么？"

    abiao "MOSA舞团比赛视频。"
    abiao "跳得太强了吧。"

    "SY本来还眯着眼。"
    "听到这个名字，瞬间清醒。"

    show sy alert at right

    sy "等等。"
    sy "再放一遍。"

    "视频里那么多人一起跳。"
    "可SY还是一眼就看见了种芒。"

    abiao "你不是吧。"
    abiao "你该不会对舞蹈突然开窍了？"

    sy "我只是……随便看看。"

    abiao "我看你像喝了假酒。"

    "几分钟后，SY已经顺着阿表的消息，问到了MOSA下一次校内演出的时间。"

    scene bg hall_inside_night
    with fade

    play music "audio/bgm/event_wait.ogg" fadein 1.2

    "到了演出那晚，SY把别凑也一起拽去了宴会厅。"
    "别凑本来没兴趣，但一听小葵可能会来，立刻答应。"

    "等节目开始前的空档里，两个人坐在座位上联机打游戏。"
    "打着打着，手机双双没电。"

    biecou "完了。"
    biecou "精神食粮断供。"

    sy "我出去透口气。"

    scene bg basement_stairs
    with fade

    "宴会厅外侧有一段往下的楼梯。"
    "SY原本只是随意一瞥，却像被什么牵住一样，一路走到了地下一层。"

    "走廊尽头，有一扇厚重的铁门。"

    play sound "audio/sfx/metal_door.ogg"

    "她刚抬手，门就从里面开了。"

    show zhongmang at center
    show sy surprised at right
    with dissolve

    sy "种芒学姐？"

    zhongmang "是你啊。"

    "地下室的光线很暗。"
    "她们隔着不到一步的距离站着，谁都没先动。"

    sy "你今天不上台吗？"

    zhongmang "这次的节目更适合小葵。"
    zhongmang "我偷个懒。"

    "她说完，像是又想起了什么。"

    zhongmang "SY。"
    zhongmang "你是来看我的吗？"

    "这一句又轻又缓，尾音还带点笑。"
    "可SY只觉得整个人像被按在原地，连呼吸都不会了。"

    sy "我……"

    "她没能把话说完。"
    "因为种芒已经往前靠了一步。"

    "她抬手碰了碰SY后颈，动作很轻。"
    "唇没有真正落下来，只是停在离锁骨极近的位置。"

    zhongmang "和那件外套一样。"
    zhongmang "你身上的味道，还是很好闻。"

    "等种芒走开以后，SY还在原地站了很久。"
    "久到像一块被高温烧透的金属。"

    scene bg hall_inside_night
    with fade

    show biecou at left
    show sy dazed at right
    with dissolve

    biecou "你去哪了？"
    biecou "脸怎么这么红？"

    sy "……别凑。"
    sy "演出结束以后。"
    sy "陪我去喝酒吧。"

    "别凑盯着她看了两秒。"

    biecou "你果然是喝了假的。"

    stop music fadeout 2.0

    return

label chapter08_preview:

    scene black
    with fade

    play music "audio/bgm/ch8_theme.ogg" fadein 1.5

    centered "第八章【驯养】"

    scene bg bbq_soju_night
    with dissolve

    "肥皂是被别凑临时叫出来的。"
    "她原本以为只是普通聚餐。"
    "没想到到了以后，真正闷头灌酒的人居然是SY。"

    show feizao concerned at left
    show sy flushed at center
    show biecou worried at right
    with dissolve

    feizao "有心事可以说。"
    feizao "没必要拿烧酒和自己较劲。"

    sy "队长也喝。"

    biecou "你别笑。"
    biecou "她今天真的不太正常。"

    "可SY看上去明明已经醉了，动作却还稳得离谱。"
    "一个小时后，先倒下的反而是别凑和肥皂。"

    scene bg street_night
    with fade

    "SY结完账，冷静地联系了另外两个队友来捞人。"
    "别凑个子小，被拎走得最轻松。"
    "真正麻烦的是喝到失去意识的肥皂。"

    scene bg senior_dorm_gate_night
    with dissolve

    "她们好不容易把人送到大三宿舍门口，却被宿管拦了下来。"
    "僵持间，一个熟悉的声音从楼道里传来。"

    show yangwenming formal at center
    with dissolve

    yangwenming "把肥皂交给我。"
    yangwenming "她住我隔壁。"

    "SY下意识想拒绝。"
    "可杨文明只是看了她一眼，那目光冷静得不容反驳。"

    scene bg dorm_hall_night
    with fade

    "最后，肥皂还是被杨文明接了过去。"
    "她一路拖着这个高她半头的醉鬼，表情几乎写满了忍耐。"
    "可真正把人安顿到床上以后，她动作又放轻了。"

    "她替肥皂擦了脸，把乱掉的被角掖好。"
    "站在床边静了很久，才转身离开。"

    scene bg dorm_night
    with fade

    play music "audio/bgm/restless_night.ogg" fadein 1.0

    "而SY一回宿舍就倒在床上。"
    "那一夜她做了个混乱又滚烫的梦。"
    "梦里没有清晰的画面，只有靠得过近的呼吸，和一遍遍响在耳边的名字。"

    zhongmang "SY。"

    scene bg bathroom_morning
    with fade

    show sy embarrassed at center
    with dissolve

    "第二天醒来，她整个人都不对劲。"
    "阿表还在刷牙，就听见上铺传来一声过分清醒的惊叫。"

    abiao "你又怎么了？"

    sy "没事。"
    sy "……真的没事。"

    "可她照镜子的时候，还是第一次认真意识到。"
    "自己好像已经没办法再把种芒当成普通学姐看了。"

    scene bg biecou_room_day
    with fade

    "另一边，别凑宿醉醒来以后，脑子像被人用锤子砸过。"
    "可今天下午，她和小葵约好了去看电影。"

    "于是她洗澡、吹头发、挑衣服、喷香水。"
    "认真得像要去参加人生第一次重要面试。"

    biecou "(至少不能看起来太像个野孩子。)"

    scene bg cinema_lobby_evening
    with dissolve

    "电影是《小王子》。"
    "小葵穿着白衬衫站在人群里，安静得像一束被单独打亮的光。"

    show xiaokui calm at left
    show biecou at right
    with dissolve

    "别凑抱着爆米花坐下后，几乎没怎么看电影。"
    "她更在意的是，小葵坐在自己身边时，连呼吸都变得很轻。"

    "散场以后，小葵明显有些低落。"
    "别凑不知道该怎么安慰，只能陪她慢慢走。"

    biecou "(不管你心里是不是还留着别的人。)"
    biecou "(我都会一直在。)"

    stop music fadeout 2.0

    return

label chapter09_preview:

    scene black
    with fade

    play music "audio/bgm/ch9_theme.ogg" fadein 1.5

    centered "第九章【暗伏】"

    scene bg dance_room_day
    with dissolve

    "年末活动扎堆，舞室几乎天天亮到很晚。"
    "这天止水和小葵都有别的安排，只有种芒一个人留在地下舞室。"

    show zhongmang at center
    with dissolve

    "她对着镜子跳了几遍新扒的舞。"
    "动作并不差。"
    "可她自己知道，还差一点想要的力度。"

    zhongmang "(果然这段更适合止水。)"

    "练累以后，她坐到地板上刷手机。"
    "先是舞团账号的后台。"
    "再是那些永远看不完、也永远不值得看的评论。"

    "夸奖、建议、酸话。"
    "还有一些让人一眼就反胃的下流发言。"

    zhongmang "真无聊。"

    "她把那些字一句句划过去。"
    "舞蹈在她眼里是表达，是语言，是锋利又漂亮的东西。"
    "不是别人拿来意淫的素材。"

    scene bg phone_screen_dark
    with dissolve

    "可下一条动态，还是让她停住了。"
    "那是一组转发很高的比赛抓拍。"
    "标题写着: 樱花女大篮球女神。"

    "照片里的人是SY。"
    "一张是她起跳上篮。"
    "另一张是中场休息时，汗湿头发往后拨开后露出来的笑。"

    zhongmang "(果然。)"

    "评论区里一大片夸赞。"
    "帅。好看。想认识。想告白。"
    "种芒看着那些字，忽然觉得有点刺眼。"

    scene bg dance_room_night
    with fade

    "她本来以为自己只是觉得SY有趣。"
    "像漂亮木佛里藏着一头尚未被唤醒的野兽。"
    "那种反差足够罕见，所以值得她多看几眼，多拨几下。"

    "可现在她发现，不只是这样。"

    zhongmang "我好像……有点舍不得让别人看了。"

    "种芒很少承认自己的占有欲。"
    "她更习惯把一切包装成游戏。"
    "可游戏若是开始让人认真，就没那么容易抽身了。"

    "她看着镜子里自己的倒影，忽然轻轻笑了一下。"

    zhongmang "SY。"
    zhongmang "你到底会先成为木佛，还是先变成野兽呢。"

    stop music fadeout 2.0

    return

label chapter10_preview:

    scene black
    with fade

    play music "audio/bgm/ch10_theme.ogg" fadein 1.5

    centered "第十章【光影】"

    scene bg student_office_day
    with dissolve

    "年末的学生会办公室，永远像打不完的仗。"
    "申请表、比赛材料、预算单、活动审批。"
    "每一样都等着杨文明处理。"

    show yangwenming formal at center
    with dissolve

    "她已经连着几天睡得很少。"
    "桌上的咖啡凉了又续，续了又凉。"
    "可她还是坐得笔直，像什么都不能把她压垮。"

    "因为在所有人眼里，杨文明本来就该是完美的。"
    "她成绩最好，办事最稳，站在任何场合都像理所当然的中心。"

    scene bg childhood_memory
    with fade

    "只有她自己知道，自己这道光旁边，一直都有一道影子。"
    "那道影子叫肥皂。"

    "她们从小一起长大。"
    "一个认真、克制、总是想把所有事做到最好。"
    "一个随性、懒散，却总在她快撑不住的时候出现。"

    "肥皂像是她的反面。"
    "可偏偏也是最久的陪伴。"

    scene bg student_office_night
    with dissolve

    "这也是为什么，当她看到篮球队这一季的赛程和数据时，还是没办法真正袖手旁观。"
    "下一场对手是阿尔法大学。"
    "那是一支平均身高、身体对抗和战术成熟度都远在樱花队之上的队伍。"

    "尤其是她们常用的人墙防守，几乎正好克制SY和别凑的突进配合。"

    "杨文明把资料翻到最后，沉默很久。"
    "然后她把整理好的笔记，托人带去了篮球队。"

    scene bg feizao_room_evening
    with fade

    show feizao serious at center
    with dissolve

    "肥皂收到那份资料时，愣了好一会儿。"
    "队友只说了一句。"

    "这是杨文明托我给你的。"

    "她没有多解释。"
    "可那一瞬间，肥皂像是忽然被什么轻轻顶了一下心口。"

    scene bg dorm_evening
    with fade

    play music "audio/bgm/pre_match_calm.ogg" fadein 1.0

    "与此同时，SY为了让自己最近过热的大脑冷下来，开始在寝室里听佛经。"
    "阿表看她盘腿坐着戴耳机的模样，差点以为室友要原地出家。"

    abiao "你最近真的很吓人。"
    abiao "先是喝酒，再是发呆，现在开始修行。"

    sy "我只是想安静一点。"

    abiao "那你安静得也太有仪式感了。"

    scene bg training_field_evening
    with fade

    "离比赛只剩两天，篮球队开始最后的针对性训练。"
    "肥皂把那份资料拆开讲给所有人听，从对手身高到惯用路线，一条条分析。"

    show feizao serious at left
    show sy focused at center
    show biecou at right
    with dissolve

    feizao "她们最喜欢堆禁区。"
    feizao "我们不能硬闯。"
    feizao "这场改打外拉和转移，先把她们的人墙撕开。"

    "SY很快听懂了。"
    "别凑也听懂了。"
    "所以训练结束后，当肥皂单独把她叫住时，她其实已经猜到了大半。"

    feizao "别凑。"
    feizao "这场你可能要先替补。"

    "空气静了一秒。"

    biecou "行啊。"
    biecou "只要能赢，我打多久都可以。"

    "她笑得很亮。"
    "亮得让肥皂差点没能及时移开视线。"

    scene bg office_window_night
    with fade

    show yangwenming formal at center
    with dissolve

    "另一边，杨文明站在办公室窗前，看着远处训练场还亮着的灯。"
    "她没有发消息，也没有留下更多解释。"
    "可她知道，肥皂一定会明白。"

    "光照得越亮，影子就越深。"
    "可有些人之所以一直站在光里，恰恰是因为影子从未真正离开。"

    stop music fadeout 2.0

    return
