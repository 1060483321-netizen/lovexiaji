init -5:
    image main_menu = "assets/menu_bg.png"

init -6 python:
    def portrait(path, target_height=600):
        _width, height = renpy.image_size(path)
        scale = min(1.0, float(target_height) / float(height))
        return Transform(path, zoom=scale, yalign=1.0)

    def sy_variant():
        return ConditionSwitch(
            "sy_outfit == 'home'", portrait("assets/SY居家.png"),
            "sy_outfit == 'date'", portrait("assets/SY约会.png"),
            "sy_outfit == 'basketball'", portrait("assets/SY篮球.png"),
            "sy_outfit == 'suit'", portrait("assets/SY西装.png"),
            "True", portrait("assets/SY日常.png"),
        )

    def biecou_variant():
        return ConditionSwitch(
            "biecou_outfit == 'home'", portrait("assets/居家别凑.png"),
            "biecou_outfit == 'practice'", portrait("assets/练习别凑.png"),
            "biecou_outfit == 'stage'", portrait("assets/演出别凑.png"),
            "biecou_outfit == 'basketball'", portrait("assets/别凑篮球版.png"),
            "True", portrait("assets/别凑常服.png"),
        )

default sy_outfit = "daily"
default biecou_outfit = "casual"

image abiao = portrait("assets/abiao.png")
image abiao curious = portrait("assets/abiao.png")
image abiao excited = portrait("assets/abiao.png")
image abiao sick = portrait("assets/abiao.png")
image abiao smile = portrait("assets/abiao.png")
image abiao surprised = portrait("assets/abiao.png")
image abiao talk = portrait("assets/abiao.png")
image abiao tired = portrait("assets/abiao.png")
image abiao worried = portrait("assets/abiao.png")
image biecou_casual = portrait("assets/别凑常服.png")
image biecou_basketball = portrait("assets/别凑篮球版.png")
image biecou_home = portrait("assets/居家别凑.png")
image biecou_practice = portrait("assets/练习别凑.png")
image biecou_stage = portrait("assets/演出别凑.png")
image biecou = biecou_variant()
image biecou angry = biecou_variant()
image biecou down = biecou_variant()
image biecou dribble = biecou_variant()
image biecou exhausted = biecou_variant()
image biecou frustrated = biecou_variant()
image biecou guilty = biecou_variant()
image biecou nervous = biecou_variant()
image biecou pleading = biecou_variant()
image biecou serious = biecou_variant()
image biecou shocked = biecou_variant()
image biecou sing = biecou_variant()
image biecou smile = biecou_variant()
image biecou stiff = biecou_variant()
image biecou talk = biecou_variant()
image biecou worried = biecou_variant()
image daru = portrait("assets/daru.png")
image daru upset = portrait("assets/daru.png")
image feizao awkward = portrait("assets/feizao.png")
image feizao concerned = portrait("assets/feizao.png")
image feizao grin = portrait("assets/feizao.png")
image feizao serious = portrait("assets/feizao.png")
image feizao worried = portrait("assets/feizao.png")
image mother normal = Text("母亲", font="SourceHanSansLite.ttf", size=72, color="#ffffff", outlines=[ (2, "#000000", 0, 0) ])
image mother worried = Text("母亲", font="SourceHanSansLite.ttf", size=72, color="#ffffff", outlines=[ (2, "#000000", 0, 0) ])
image sy_daily = portrait("assets/SY日常.png")
image sy_home = portrait("assets/SY居家.png")
image sy_date = portrait("assets/SY约会.png")
image sy_basketball = portrait("assets/SY篮球.png")
image sy_suit = portrait("assets/SY西装.png")
image sy alert = sy_variant()
image sy alone = sy_variant()
image sy awkward = sy_variant()
image sy dazed = sy_variant()
image sy determined = sy_variant()
image sy down = sy_variant()
image sy embarrassed = sy_variant()
image sy fierce = sy_variant()
image sy flushed = sy_variant()
image sy focused = sy_variant()
image sy kneel = sy_variant()
image sy lying = sy_variant()
image sy neutral = sy_variant()
image sy shocked = sy_variant()
image sy sleepy = sy_variant()
image sy smile = sy_variant()
image sy startled = sy_variant()
image sy strained = sy_variant()
image sy stunned = sy_variant()
image sy surprised = sy_variant()
image sy tense = sy_variant()
image sy tired = sy_variant()
image xiaokui calm = portrait("assets/xiaokui.png")
image xiaokui sad = portrait("assets/xiaokui.png")
image xiaokui serious = portrait("assets/xiaokui.png")
image xiaokui startled = portrait("assets/xiaokui.png")
image yangwenming formal = portrait("assets/yangwenming.png")
image yuhui = portrait("assets/yuhui.png")
image zhishui angry = portrait("assets/zhishui.png")
image zhishui cool = portrait("assets/zhishui.png")
image zhongmang = portrait("assets/zhongmang.png")

image bg airport_home = "assets/campus_bg.png"
image bg arena_corner_day = "assets/basketball_arena.png"
image bg arena_exterior_day = "assets/basketball_arena.png"
image bg arena_stands_day = "assets/basketball_arena.png"
image bg backstage_dark = "assets/school_stage.png"
image bg backstage_evening = "assets/school_stage.png"
image bg backstage_hall = "assets/school_stage.png"
image bg band_venue_backstage = "assets/school_stage.png"
image bg bandroom_smoke = "assets/campus_bg.png"
image bg barbecue_night = "assets/street_night.png"
image bg barbecue_restaurant_night = "assets/street_night.png"
image bg basement_bandroom = "assets/campus_bg.png"
image bg basement_stairs = "assets/campus_bg.png"
image bg basketball_arena_day = "assets/basketball_arena.png"
image bg basketball_court_day = "assets/basketball_arena.png"
image bg basketball_court_match = "assets/basketball_arena.png"
image bg bath_exit_night = "assets/street_night.png"
image bg bathroom_morning = "assets/campus_bg.png"
image bg bathroom_steam = "assets/campus_bg.png"
image bg bbq_night = "assets/street_night.png"
image bg bbq_soju_night = "assets/street_night.png"
image bg beef_intestine_room_night = "assets/cafeteria_bg.png"
image bg bench_area_day = "assets/campus_bg.png"
image bg bench_day = "assets/campus_bg.png"
image bg biecou_room_dark = "assets/dorm_bg.png"
image bg biecou_room_day = "assets/dorm_bg.png"
image bg billiards_day = "assets/campus_bg.png"
image bg buffet_counter = "assets/cafeteria_bg.png"
image bg cafe_day = "assets/cafeteria_bg.png"
image bg cafeteria_close = "assets/cafeteria_bg.png"
image bg cafeteria_day = "assets/cafeteria_bg.png"
image bg cafeteria_road_day = "assets/cafeteria_bg.png"
image bg campus_crossroad_sunset = "assets/campus_bg.png"
image bg campus_gate_day = "assets/school_gate_bg.png"
image bg campus_path_day = "assets/campus_bg.png"
image bg campus_road_evening = "assets/campus_bg.png"
image bg campus_spring_day = "assets/campus_bg.png"
image bg chairman_office_day = "assets/student_office.png"
image bg chat_screen_night = "assets/street_night.png"
image bg childhood_memory = "assets/campus_bg.png"
image bg christmas_street = "assets/street_night.png"
image bg cinema_lobby_evening = "assets/street_night.png"
image bg city_car_day = "assets/campus_bg.png"
image bg city_road_day = "assets/campus_bg.png"
image bg comic_cafe_day = "assets/campus_bg.png"
image bg comic_con_day = "assets/school_stage.png"
image bg comic_con_exit_evening = "assets/school_stage.png"
image bg conference_hall_day = "assets/school_stage.png"
image bg corridor_day = "assets/campus_bg.png"
image bg dance_room_day = "assets/dance_room.png"
image bg dance_room_evening = "assets/dance_room.png"
image bg dance_room_exit_evening = "assets/dance_room.png"
image bg dance_room_night = "assets/dance_room.png"
image bg dinner_table = "assets/cafeteria_bg.png"
image bg dorm_bed_night = "assets/dorm_bg.png"
image bg dorm_corridor_evening = "assets/dorm_bg.png"
image bg dorm_corridor_morning = "assets/dorm_bg.png"
image bg dorm_corridor_night = "assets/dorm_bg.png"
image bg dorm_dark_day = "assets/dorm_bg.png"
image bg dorm_dark_night = "assets/dorm_bg.png"
image bg dorm_day = "assets/dorm_bg.png"
image bg dorm_evening = "assets/dorm_bg.png"
image bg dorm_gate_day = "assets/dorm_bg.png"
image bg dorm_hall_day = "assets/dorm_bg.png"
image bg dorm_hall_night = "assets/dorm_bg.png"
image bg dorm_hallway_evening = "assets/dorm_bg.png"
image bg dorm_morning = "assets/dorm_bg.png"
image bg dorm_night = "assets/dorm_bg.png"
image bg dorm_path_day = "assets/dorm_bg.png"
image bg dream_white = "assets/campus_bg.png"
image bg drink_shop_evening = "assets/cafeteria_bg.png"
image bg empty_court_evening = "assets/campus_bg.png"
image bg equipment_room_day = "assets/campus_bg.png"
image bg external_affairs_office = "assets/student_office.png"
image bg family_dinner_night = "assets/dorm_bg.png"
image bg feizao_home_night = "assets/dorm_bg.png"
image bg feizao_room_day = "assets/dorm_bg.png"
image bg feizao_room_evening = "assets/dorm_bg.png"
image bg feizao_room_night = "assets/dorm_bg.png"
image bg flashback_alley = "assets/campus_bg.png"
image bg flashback_home = "assets/campus_bg.png"
image bg flashback_window = "assets/campus_bg.png"
image bg gym_exit_sunset = "assets/basketball_arena.png"
image bg gym_interior_day = "assets/basketball_arena.png"
image bg hall_inside_night = "assets/school_stage.png"
image bg hall_outside_evening = "assets/school_stage.png"
image bg haunted_exit = "assets/campus_bg.png"
image bg haunted_school = "assets/campus_bg.png"
image bg home_livingroom = "assets/dorm_bg.png"
image bg hotel_hall_morning = "assets/dorm_bg.png"
image bg hotel_room_morning = "assets/dorm_bg.png"
image bg hotel_room_night = "assets/dorm_bg.png"
image bg infirmary_day = "assets/infirmary.png"
image bg infirmary_night = "assets/infirmary.png"
image bg instrument_shop_day = "assets/campus_bg.png"
image bg internet_cafe_day = "assets/campus_bg.png"
image bg internet_cafe_night = "assets/campus_bg.png"
image bg izakaya_night = "assets/street_night.png"
image bg ktv_after = "assets/campus_bg.png"
image bg ktv_game = "assets/campus_bg.png"
image bg ktv_room_night = "assets/campus_bg.png"
image bg late_dinner_night = "assets/street_night.png"
image bg library_day = "assets/classroom_bg.png"
image bg milktea_shop_night = "assets/street_night.png"
image bg noodle_shop_night = "assets/street_night.png"
image bg office_files_day = "assets/student_office.png"
image bg office_window_night = "assets/student_office.png"
image bg pharmacy_night = "assets/street_night.png"
image bg phone_screen_dark = "assets/campus_bg.png"
image bg plaza_stage_evening = "assets/campus_bg.png"
image bg plaza_sunset = "assets/campus_bg.png"
image bg practice_end_evening = "assets/dance_room.png"
image bg restaurant_day = "assets/cafeteria_bg.png"
image bg rollercoaster_queue = "assets/campus_bg.png"
image bg rollercoaster_ride = "assets/campus_bg.png"
image bg school_gate_day = "assets/school_gate_bg.png"
image bg seafood_restaurant_night = "assets/cafeteria_bg.png"
image bg senior_dorm_door = "assets/dorm_bg.png"
image bg senior_dorm_gate_night = "assets/dorm_bg.png"
image bg senior_dorm_inside = "assets/dorm_bg.png"
image bg senior_dorm_morning = "assets/dorm_bg.png"
image bg senior_dorm_night = "assets/dorm_bg.png"
image bg stage_award = "assets/school_stage.png"
image bg stage_blackout = "assets/school_stage.png"
image bg stage_glow = "assets/school_stage.png"
image bg stage_spotlight = "assets/school_stage.png"
image bg street_night = "assets/street_night.png"
image bg student_office_day = "assets/student_office.png"
image bg student_office_night = "assets/student_office.png"
image bg supermarket_evening = "assets/street_night.png"
image bg sushi_room_night = "assets/cafeteria_bg.png"
image bg taxi_night = "assets/street_night.png"
image bg tea_restaurant_day = "assets/cafeteria_bg.png"
image bg themepark_gate_day = "assets/school_gate_bg.png"
image bg themepark_path_day = "assets/campus_bg.png"
image bg track_winter_night = "assets/campus_bg.png"
image bg training_field_day = "assets/campus_bg.png"
image bg training_field_evening = "assets/campus_bg.png"
image bg training_field_morning = "assets/campus_bg.png"
image bg training_field_winter = "assets/campus_bg.png"
image bg xiaokui_room_day = "assets/xiaokui_room.png"
image bg xiaokui_room_night = "assets/xiaokui_room.png"
image bg zhongmang_home_night = "assets/zhongmang_room.png"
image bg zhongmang_room_night = "assets/zhongmang_room.png"
