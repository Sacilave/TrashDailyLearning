label start:
    "选择要测试的标签"
    menu:
        "测试":
            jump test_
        "文本":
            jump text_
        "Python代码块":
            jump python_
        "图像(初级)":
            jump image_
        "图像(高级)":
            jump image2_
        "转场":
            jump transition_
        "位置":
            jump position_
        "下一页":
            jump start2
label start2:
    menu:    
        "音乐和音效":
            jump music_
        "pause语句":
            jump pause_
        "分支":
            jump choice_
        "上一页":
            jump start

label test_:
    image plain = "plain.png"
    show plain:
        xanchor 0
        yanchor 0
    "显示 - 1"
    hide plain
    
    jump start


# 角色对象(初级)
    define daxiong = Character('大雄', color="#FFC0CB")  # 这里新建了一个角色叫做：Wdnmd，颜色为 #FFC0CB (粉红)
    define duolaameng = Character('哆啦A梦', color="#8470FF")
    define me = Character('我', color="#FFFFFF")  # 同理
    define speaker = Character('解释员', color="#FF6A6A")


# 角色对象(高级)
    define sacilave = Character('Sacilave', who_size = 25, what_size = 35)
    sacilave "hello, world !"
    ### 在 Ren'Py 中，有 who 和 what 这两个角色对象的属性
    ### what 指的是对象说的话(角色说的话的颜色、字体大小等)，上方的 what_size 指的就是角色说的话的字体大小
    ### who 指的是对象自己(角色名称的颜色、字体大小等)，上方的 who_size 指的就是角色名称的字体大小
    ## 除此之外还有很多其他的属性
    ## window_background(设置对话框背景) : 设置一个文件路径，如果设置为 None , 便为隐藏消息框(window_background=None)
    define sylvie = Character('Sylvie', window_background = "gui/textbox2.png")
    sylvie "使用：window_background(设置对话框背景)"
    ## who_color(角色颜色) / what_color(角色对话颜色) : 设置一个16进制颜色
    define sylvie01 = Character('Sylvie01', who_color = "#c8ffc8", what_color = "#ffc8c8")
    sylvie01 "使用：who_color(角色颜色) / what_color(角色对话颜色)"
    ## who_bold(粗体) / what_italic(斜体) : bold 和 italic 两个属性对 who 和 what 都适用
    define sylvie02 = Character('Sylvie02', who_bold = True, what_italic = True)
    sylvie02 "使用：who_bold(粗体) / what_italic(斜体)"
    ## who_outlines(外边框) : 语法为 who_outlines=[( 粗细, "16进制颜色", x偏移, y偏移 )]
    define sylvie03 = Character('Sylvie03', who_outlines=[(2, "008000", 1, 1)], what_outlines=[(1, "008000", 3, 1)])
    sylvie03 "使用：who_outlines(外边框)"
    ## prefix(前方自动追加) / suffix(后方自动追加) : 都适用与 who 和 what
    define sylvie04 = Character('Sylvie04', what_prefix='Wdnmd, ', what_suffix='呐')
    sylvie04 "使用：prefix(前方自动追加) / suffix(后方自动追加)"
    ## font(更改字体) : 适用于 who 和 what，如果角色字体都要一样就去 option.rpy 里面改
    define sylvie05 = Character('Sylvie05', who_font="RunningHand.ttf")
    sylvie05 "使用：font(更改字体)(更改了 who 的字体为 RunningHand.ttf \[名字是自编的\] )"

    ### 更改角色说话时的动画效果
    define config.say_attribute_transition = dissolve  # 现在设置为了 dissolve


# 动画
    transform transform01:
        alpha 0.0  # alpha 为透明度的控制
        linear 1.0 alpha 1.0  # linear 可以控制一个时间范围(比如这一行就是：在 1.0 秒钟内透明度调节到 1.0)
        linear 1.0 alpha 0.0  # 这里就是：在 1.0 秒钟透明度调节到 0.0
        repeat  # 该语句可以使这整个标签全部重复(当前便可以使这个动画无限重复达到渐淡渐出的闪烁的效果)


# 文本
label text_:
    define human01 = Character('human01')
    "Sylvie"  "Hello World !"  # 这里的两个字符串：前一个 是说话的人，后一个是 说的东西
    human01 "AMD, YES !!!"  # 这里使用了上面的角色 human01 并说：AMD, YES !!!
    "Bull shit, Intel is the best"
    "可以使用文本标签改变样式, {b}这是粗体{/b}, {i}这是斜体{/i}, {s}这是删除线{/s}, {u}这是下划线{/u}"
    "{a=https://www.bilibili.com}也可以绑定超链接{/a}"
    "{a=jump:test}也可以跳转到其他标签{/a}"  # 注意在 jump: 语法后面不要使用空格(如 jump: test 是不行的)
    "{alpha=0.4}还可以调节透明度{/alpha}"
    "{color=#0080c0}还能变颜色{/color}"  # 必须使用16进制颜色(当前为蓝色)
    "{cps=25}cps标签可以改变文字速度(现在速度为25){/cps}{cps=1}现在速度为 1{/cps}"
    "甚至可以修改一段字体 -- {font=DejaVuSans-Bold.ttf}Zhe font is DejaVuSans-Bold now{/font}"
    "也可以更改{size=+10}字体大小！{/size}{size=-10}使用 =- 和 =+ 符号可以按原来大小放大缩小{/size}"
    "space可以插入{space=30}一段空白，{vspace=30}可以上下的距离空白"
    "p标签可以进行换行，{p}要再次点击才能显示文本, 还可以延迟指定时间{p=1.5}延迟后再显示"
    "w标签 与 p标签 相同，但是不换行{w}点击后显示{w=1.0}延迟显示"
    "[value01]"  # 这里使用 中括号 来显示中括号内指定的变量值
    $ value01 = False  # 使用 $ 符号进行运行 python 代码段(此处重新赋值 value01 为 False)
    "[value01]"  # 重新就显示为了 False.
    jump start


# Python代码块
    define value01 = True  # 也可以定义一个变量
    define value02 = 1  # 也和 Python 一样可以使用多种数据类型
    label python_:
        # 在 Ren'Py 中可以使用 python 语句
        $ value01  = True  # 使用 $ 符号使这一整行都作为 Python 代码运行
        "value01 的值：[value01]"
        python:
            value02 = value02 + 1  # 也可以用 Python标签 进行多行python代码运行
        "value02 的值：[value02]"
        jump start


# 图像(初级)
    image duolaameng = "duolaameng normal.jpg"  # 图像可以使用 image 语句建立一个指定图像的标签 (注意 image 语句加载必须在最前面)
    label image_:
        # 对于图片：要把图片放在 项目文件夹下的 image 文件夹内，命名规则为: 标签(tag) 属性(attribute)
        # 举个例子：有一个是地球的背景命名可以为：bg earth ，一个叫做 Sylvie 的角色动作为 吃 ，表情为 笑 命名可以为：sylvie eat smile
        scene bg grass  # scene 语句基本用于背景，因为它会覆盖掉原来的所有图片(注意是所有图片！)，该语句把名为 bg test 的图片显示了出来

        show daxiong normal  # show 语句基本用于角色，因为它不会覆盖原来的图片，该语句把名为 daxiong normal 的图片显示了出来

        daxiong  "Wdnmd 哆啦A梦"

        hide daxiong # hide 语句可以使图像隐藏，该语句把 duolaameng 的图片隐藏了

        show duolaameng

        duolaameng  "Wdnmd 大雄"

        show daxiong normal  # 之前定义了 logo 这个图像，现在直接显示出来

        daxiong "不错"
        jump start


# 图像(高级)
    ### 对话结尾的结尾符号闪烁是如何实现的
        image img01:
            "images/img01.png"
            size(25, 25)  # 控制该图片大小为 25x25 像素
            transform01  # 这里使用了 transform01 这个效果
        # 创建角色时使用 ctc 在对话框增加图片，ctc 也有许多属性比如 ctc_position 可以调节位置
        # ctc 可以用于制作类似一段话结尾有一个结束符号的效果
        define chr01 = Character('chr01', ctc = 'img01', ctc_position = 'nestled')
        label image2_:
            chr01 "使用了 ctc 呢"

    ### 对于角色图片不同表情在每一段对话都要变化的情况
        # 这种情况下的图片变化次数会十分的多，所以通常不用 show 和 hide 语句
        define monika = Character('Monika', image = 'monika_img')
        image monika_img a = 'monika1.png'
        image monika_img b = 'monika2.png'
        show monika_img a with dissolve  # 首先显示出来 monika_img a 的图像
        monika a "en, yes"  # 这里相当于使用了 monika角色 并显示了 monika_img a
        monika b "en, no"   # 这里相当于使用了 monika角色 并显示了 monika_img b
        monika a "I'm fucking good"
        monika b "except you leave me alone"
        hide monika_img with dissolve  # 这里直接隐藏了 monika 的图像
    
    ### 图像的位置
        image plain = "plain.png"
        show plain:
            zoom 2.0  # zoom : 使图像放大一定倍数(当前放大3.0倍)
            alpha 0.5  # alpha : 修改透明度
            rotate 45  # rotate : 顺时针旋转一定角度
            xcenter 0.5  # xcenter : 设置图像中心点的x轴位置(设置的数值为0~1, 从左上角开始为x=0,y=0; 向下y增大，向右x增大)
            ycenter 0.5  # ycenter : 设置图像中心点的y轴位置
        "第一次显示"
        hide plain

        show plain:
            xalign 0  # xalign : 设置图像整体的x轴位置(坐标范围与 xcenter 相同)
            yalign 1  # yalign : 设置图像整体的y轴位置(但这个是整体的移动,图片放到边缘不会超出边框)
        "第二次显示"
        hide plain

        show plain:
            xoffset 100  # offset : 使图片偏移一定像素值，向右为正数，向左为负数(当前便为向右偏移100像素)
            xanchor 0.5  # anchor : 锚点坐标(图像的最左上角作为坐标)进行移动
            yanchor 0.5  # 比如现在的 xanchor 和 yanchor 都为 0.5 时，图像的最左上角就会在中央
        "第三次显示"
        hide plain
        
        show plain at right  # 也可以使用 at 关键字确定多个固定的方位(这个默认以中心点定点)
        "第四次显示"
        hide plain
        """ 默认的位置
        +-----------------------------------------------------------------------------+
        | topleft/reset                       top                            topright |
        |                                                                             |
        |                                                                             |
        |                                                                             |
        |                                                                             |
        |                                                                             |
        |                                                                             |
        |                                                                             |
        |                                  truecenter                                 |
        |                                                                             |
        |                                                                             |
        |                                                                             |
        |                                                                             |
        |                                                                             |
        |                                                                             |
        | left                           center/default                         right |
        +-----------------------------------------------------------------------------+
        """

    ### 图像的运动
        """ 各种运动方式
        linear : 线性运动
        ease : 缓动函数(慢 -> 快 -> 慢)
        easein : (快 -> 慢)
        easeout : (慢 -> 快)
        pause : 暂停
        time : 控制一个固定时间，到达固定时间会结束动画
        parallel / contains : 同时运行区块(当一个对象需要进行很多效果时，比如要旋转，放大，平移，可以使用parallel)
        """
        image plain0:
            "plain.png"
            move01
        transform move01:
            xalign 0.0
            yalign 1.0
            block:  # block 可以对一块代码封装
                linear 2.0 xalign 1.0 yalign 0.0  # linear : 线性运动(正常的匀速直线运动)，使 xalign 运动到1.0, yalign 运动到 0.0
                linear 2.0 xalign 0.0 yalign 1.0
                repeat
            time 8.0  # 限制上面的动画只执行8.0秒，8.0秒到达后直接停止
        show plain0
        "开始了运动"
        hide plain0
        "隐藏了图片"
        image plain1:
            "plain.png"
            move02
        transform move02:
            xalign 0.0
            yalign 0.5
            parallel:
                ease 1.5 xalign 1.0
                ease 1.5 xalign 0.0
                repeat
            parallel:
                linear 1.5 zoom 2.0
                linear 1.5 zoom 0.0
                repeat
            parallel:
                linear 1.5 rotate 360
                linear 1.5 rotate -360
                repeat
        show plain1
        "又开始了运动"
        hide plain1
        
        ### 注意！！！Ren'Py支持所有的 RobertPenner(缓冲函数)(类似于linear,ease等的运动函数)
        ### 可参考 https://easings.net/ 查看所有函数图像

    ### 封装图像的变换和效果
        # 如果每一次都要对一个图像显示进行多个效果会很麻烦，所以可以封装为一个函数
        transform re_left:  # 先把这个效果封装
            xalign 0.0
            yalign 1.0
        transform re_center:  # 同理, 也封装了一个效果
            xcenter 0.5
            ycenter 0.5
        image plain2:  # 再把这个效果添加进图像并封装为一个 image对象
            "plain2.png"
            re_left
        show plain at re_left  # 此时可以直接使用这个效果
        "显示了红色的方片，通过 at 关键字使用了 re_left (自己封装的)效果"
        show plain at re_center  # 此时可以直接使用这个效果
        "显示了红色的方片，通过 at 关键字使用了 re_center (自己封装的)效果"
        show plain2  # 对于已经把效果封装进图像对象，使用这个对象就不用再添加效果了
        "显示了绿色的方片，直接显示了封装了 文件路径 和 re_left效果 的一个 image对象"

        

# 转场
    label transition_:
        # 因为图片显示十分生硬可以使用效果进行转场
        scene bg grass
        with fade  # 使用 with 语句，后面的 fade(褪去) 是一个效果

        show duolaameng
        with dissolve  # dessolve(溶解) 效果

        duolaameng "nmsl"

        me "啊"

        # 接着如果想让两个图像显示的效果相同
        scene bg grass
        show daxiong normal
        with fade

        # 如果想要一个无效果一个有效果可以使用 None(无) 效果
        scene bg grass
        with None
        show duolaameng
        with fade
        jump start


# 位置
    label position_:
        scene bg grass
        show duolaameng at right  # 在右端显示；还有其他方位: left(左)，right(右)，center(默认的中央位置)，truecenter(水平和垂直同时居中)
        duolaameng "使用 at 语句 切换位置！"
        show duolaameng at truecenter
        duolaameng "我透了"
        jump start


# 音乐和音效
    label music_:
        scene bg grass
        show daxiong normal
        with fade

        play music "./audio/bgm01.mp3" fadeout 1.0 fadein 1.0 # 播放一个音乐，会重复播放 (使用 fadeout 淡出，fadein 淡入 新音乐)
        play sound "./audio/fuck you.mp3"  # 播放一个音效，不会重复播放
        daxiong "FUCK YOU !!!"
        queue music "./audio/boy next door.mp3"  # queue 语句是选择在当前音乐播放玩后播放的音乐
        daxiong "boy next door"
        stop music  # 停止播放，这个也可使用 fadeout 进行淡出
        daxiong "停了"
        jump start


# pause 语句
    label pause_:
        pause 3.0  # 使用 pause 语句并加上数字可以暂停指定秒数(如当前是暂停 3 秒)
        daxiong "暂停3秒完成"
        pause  # 如果直接使用 pause 语句会一直暂停直到出现鼠标点击事件
        daxiong "暂停结束"
        jump start


# 进行分支
    label choice_:
        menu:  # menu 语句用来选择分支
            "选择一":
                jump choice01  # jump 语句用来跳转 (这里跳转到了 choice01)
            "选择二":
                jump choice02  # jump 语句用来跳转 (这里跳转到了 choice02)
    label choice01:
        speaker " 选择了\"选择一\" "  # 这里的 \ 是转义符(与 python 的转义符相同)
        jump last
    label choice02:
        speaker " 选择了\"选择二\" "
        jump last
    label last:
        speaker "选择结束"

    jump start


# 使用 default、Python和 if 语句支持 flag(标识)
    default chooseApple = False  # 使用 default 定义一个变量(不一定是一个 布尔 ，也可以是数字，字符串等)

    menu:
        "选择 Apple ":
            $ chooseApple = True  # 使用 $ 符号，可以使这一行按照 python 语法运行
        "不选择 Apple":
            $ chooseApple = False
    label game:
        if chooseApple == True:  # 如 python 语法，判断 chooseApple 这个变量是否成立
            speaker "你选择了 Apple"
        else:
            speaker "你没选择 Apple"
    jump start


# 结束游戏
    "-- The End --"
    return  # 使用 return 进行结束，在这之前最好写个结束语
