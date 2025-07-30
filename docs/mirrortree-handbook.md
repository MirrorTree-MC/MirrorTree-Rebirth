---
title: 棱镜树梦境手册
created: 2025-02-02T17:58:29+08:00
modified: 2025-07-04T11:15:47+08:00
version: 2.2.5
---

# **棱镜树梦境手册**

---

<style>
/* 目录样式优化 */
.toc-container {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  justify-content: space-between;
}

.toc-column {
  flex: 1;
  min-width: 300px;
  max-width: 48%;
}

.toc-container h3 {
  font-size: 1.1rem;
  margin: 1rem 0 0.5rem 0;
  font-weight: 600;
  color: #2c3e50;
}

.toc-container ul {
  margin: 0.5rem 0;
  padding-left: 1.2rem;
  list-style-type: none;
}

.toc-container li {
  margin: 0.3rem 0;
  line-height: 1.4;
}

.toc-container a {
  color: #0969da;
  text-decoration: none;
  font-size: 0.95rem;
}

.toc-container a:hover {
  text-decoration: underline;
}

/* 嵌套列表样式 */
.toc-container ul ul {
  margin-left: 0.8rem;
  margin-top: 0.2rem;
  padding-left: 1rem;
}

.toc-container ul ul li {
  margin: 0.2rem 0;
  font-size: 0.9rem;
}

/* 打印时仅控制分页行为，保留原样式 */
@media print {
  @page {
    size: A4;
    margin: 0; /* 页边距为0，由我们手动控制内容边距 */
  }

  html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  body {
    position: relative;
  }

  /* 添加固定背景图，每页都显示 */
  body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 210mm;
    height: 297mm;
    background: url('https://cos.bearcabbage.top/wp-content/uploads/2025/07/handbook-bg-n.png') no-repeat center center;
    background-size: 100% 100%;
    z-index: -1;
    pointer-events: none;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  /* 主内容保持标准边距 */
  .md-content {
    box-sizing: border-box;
    padding-top: 20mm;
    padding-bottom: 20mm;
    padding: 25mm;
    background: transparent;
    position: relative;
    z-index: 0;
  }

.md-content table {
    max-width: 100%;
    width: 100%;
    table-layout: fixed;
    word-break: break-word;
    overflow-wrap: break-word;
  }

  /* 限制图片宽度 */
  .md-content img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1em auto; /* 可选：居中显示 */
    page-break-inside: avoid; /* 避免分页中断图片 */
  }

  /* 强制所有元素不超过容器边界 */
  .md-content * {
    box-sizing: border-box;
    max-width: 100%;
    overflow-wrap: break-word;
    word-break: break-word;
  }

  /* 避免某些元素跨页 */
  .toc-container,
  .toc-column {
    page-break-inside: avoid;
    break-inside: avoid;
  }

  .toc-container a,
  .toc-column a {
    color: #7959BC !important;
    text-decoration: none;
  }

  /* 分页标记 */
  .page-break {
    page-break-before: always;
    break-before: page;
  }

  h1#_1 {
    text-align: center;
    font-size: 24pt;
    font-weight: bold;
    font-family: 'SimHei', 'Heiti SC', sans-serif; /* 黑体字体优先 */
    color: #582C83;
  }
  /* 可选：隐藏不需要打印的部分 */
  .md-header,
  .md-footer,
  .md-sidebar,
  .md-tabs {
    display: none !important;
  }
}
</style>

<div>

<div class="toc-container" style="display: flex; gap: 2rem; flex-wrap: wrap;">

<div class="toc-column" style="flex: 1; min-width: 200px;">

<h3>🚀 快速开始</h3>
<ul>
<li><a href="#_2">⭐️ 如何加入服务器</a></li>
<li><a href="#_3">⭐️ 服务器怎么玩</a></li>
</ul>

<h3>📚 附录</h3>
<ul>
<li><a href="#a">⌨️ 快捷键及指令</a></li>
<li><a href="#b">🏘️ 聚落说明</a></li>
<li><a href="#c">📦 模组列表</a></li>
<li><a href="#d">📋 棱镜树规范</a></li>
</ul>

</div>

<div class="toc-column" style="flex: 1; min-width: 200px;">

<h3>🎮 游戏机制</h3>
<ul>
<li><a href="#1">🌙 入梦与醒来</a></li>
<li><a href="#2">💲 经济系统</a>
<ul>
<li><a href="#20">💰 钱包</a></li>
<li><a href="#21">📦 收购</a></li>
<li><a href="#22">🛒 出售</a></li>
</ul>
</li>
<li><a href="#3">🔧 自制模组说明</a></li>
<li><a href="#4">⚙️ 游戏特性</a></li>
<li><a href="#5-bug">🐛 BUG 反馈途径</a></li>
</ul>

</div>

</div>

</div>

---

## **⭐️如何加入服务器**

1. 下载群文件`整合包及启动器`文件夹中最新的整合包 zip，解压并双击 HMCL.exe 启动游戏。
2. 注册/登录服务器（服务器地址在整合包`多人游戏`中有）：
    1. 有正版：直接加入服务器，无需任何额外操作。
    2. 没有正版：
        1. **确保你的游戏 ID 没有被任何正版账号用过**：这个网站可以查询 ID 占用[https://mcuuid.net/](https://mcuuid.net/)，输入你的 ID，如果查询不到信息就说明没有人用过。~（几乎所有离线玩家进不来都是因为这个）~
        2. 加入服务器之后根据提示输入`/register <密码> <重复密码>`注册。
        3. 以后登录的时候输入`/l <密码>`登录。

<div class="page-break"></div>
<br />

## **⭐️服务器怎么玩**

1. 你会出生在一栋小屋前，这里叫`狐狸的卧室`，是出生点大厅。

    ![foxhouse](https://cos.bearcabbage.top/wp-content/uploads/2025/07/FoxHouse.jpg)

    1. 你可以随便走走，或者拿一块木牌在雪地上留言。
    2. 左手边是`JellyNews新闻墙`，大家可以通过 QQ 群的`Mirrobot`机器人投稿新闻，展示在这里（投稿如果太长的话，可能显示不全）。
    3. 背后是卖纪念品的`雪人商店`，商店用的货币是`狐狸尾巴`，只能通过特殊活动等方式获得。

2. 当你准备好了，就可以走进这栋小屋。
    1. 屋子里有一个讲台，讲台的书里写着游戏的基本信息和棱镜树的背景故事，可以看看。
    2. 小屋左边有三个卧室，每个房间里都有一张床。

3. 右键床可以睡觉`入梦`，进入`噩梦世界`（生存世界）。你会看到一个菜单，有两个选择：
    1. **在野外的位置随机入梦**：
        - 你会被随机传送到离世界中心`3000格`以内的某个地方。
        - 入梦后你会获得一个自己的**入梦点**和`32x32x32`的安全区。
        - 如果要和朋友结伴入梦，可以在入梦前站在床边，3秒间隔内先后点击**在野外的位置随机入梦**即可（第二个人的入梦点会在第一个人周围`128格`范围内）。
    2. **在安全的聚落入梦**：
        - 你可以选择一个聚落出生，菜单上会显示聚落名字和坐标。你也可以先浏览一下[聚落介绍](#b)章节。
        - 你会被传送到聚落中心，以聚落点为中心获得`32x32x32`的安全区。
        - （可以提前在在线地图上查看聚落：[http://map.bearcabbage.top:8100/](http://map.bearcabbage.top:8100/)）

<div class="page-break"></div>
<br /><br />

  ![dreamui](https://cos.bearcabbage.top/wp-content/uploads/2025/07/DreamUI.jpg)

4.到了生存世界后，按`L`键可以打开`任务书`，查看任务和提示。然后就开始努力活着吧！

![taskbook](https://cos.bearcabbage.top/wp-content/uploads/2025/07/TaskBook.jpg)

---

!!! tip "常用工具"

    建议善用[棱镜树 Wiki](https://wiki.mirror.bearcabbage.top/)，里面会有整合包的更新日志（最新的内容会首先在此发布）以及服务器在线地图链接等。

<div class="page-break"></div><br>

## 1 **入梦与醒来**

!!! tip "入梦与醒来"

    入梦：指从出生点大厅进入游戏主世界<br>
    醒来：指从游戏主世界返回出生点大厅

- 醒来：
    - 方式：睡觉时点击聊天窗中的「醒来走走」
    - 效果：你将回到狐狸的卧室（出生点大厅）的床前
- 沉睡：
    - 方式：再点击狐狸的卧室（出生点大厅）的床回到游戏主世界
    - 效果：你将到达梦境世界（游戏主世界）「醒来」的床边

- 带新玩家结队入梦：
    - 老玩家醒来，回到狐狸的卧室，与新玩家结队入梦（老玩家先点击床，新玩家3s内点击床跟随）

- 重新入梦（特殊机制）：
    - 方式：按`L`打开任务书，第一章节「在这噩梦中，活下去」中有重新入梦的按钮，点击按钮后先后点击「对勾」和右边的「床」即可重新入梦
    - 效果：清除入梦点标记、重置玩家重生点、传送回第一次登陆服务器的出生点。你可以重新作为新玩家入梦
    - ***每人只有三次重新入梦的机会***

## 2 **经济系统**

!!! tip "货币换算"

    100 铜 = 1 银   100 银 = 1 金

### 2.0 **钱包**

#### 存钱

1. 拿着钱袋右键可以打开，钱袋内的钱币会放入背包

2. 拿着钱币（金银铜）右键可以把钱存进小钱包，在背包界面右上角（如下图所示）

#### **货币兑换**

把钱存入小钱包后，可以根据下图所示步骤，取出需要数量的金/银/铜币

<div class="page-break"></div><br>
<br /><br />

![小钱包取钱用法](https://cos.bearcabbage.top/wp-content/uploads/2025/07/moneybag.png)

!!! tip "操作技巧"

    按住Shift键点击数量调节箭头，可以每次10递增/减

### 2.1 **收购**

#### 收购机制说明

服务器使用**收购箱**（类似星露谷收集箱）的方式回收物品。

<img src="https://github.com/MirrorTree-MC/MirrorTree-Rebirth/blob/main/docs/sellingbin.png?raw=true" alt="收购箱" style="width:65px; float:left; margin-right:1em;" />

##### 收购箱合成配方

```text
木板    银币    木板
木板    木板    木板
```

##### 材料说明

- **木板**：任意种类木板（`minecraft:planks` 标签）
- **银币**：`numismatic-overhaul:silver_coin`

##### 使用方法

- 将可收购物品投入收购箱
- 每天早上8:00（游戏内时间）自动售出，钱袋直接生成在收购箱内

!!! warning "注意事项"

    - 请确保箱内有足够空间存放钱袋，避免物品丢失
    - 价格如有变动，以服务器内实时价格为准

#### 金属锭收购价格

| 物品名称     | 收购价格      | 数量    |
| ------------ | ------------- | ------- |
| 锡锭         | 40铜          | 64个    |
| 兆金锭       | 40铜          | 64个    |

<div class="page-break"></div><br>

| 物品名称     | 收购价格      | 数量    |
| ------------ | ------------- | ------- |
| 青铜锭       | 50铜          | 64个    |
| 聚爆石锭     | 70铜          | 64个    |
| 激水锭       | 80铜          | 64个    |
| 飓霆锭       | 90铜          | 64个    |
| 锰锭         | 90铜          | 64个    |
| 银锭         | 1银           | 64个    |
| 锇锭         | 1银40铜       | 16个    |
| 钯金锭       | 1银70铜       | 16个    |
| 铂金锭       | 1银90铜       | 16个    |
| 凯伯锭       | 2银20铜       | 16个    |
| 符石锭       | 2银60铜       | 16个    |
| 韧钢锭       | 2银70铜       | 16个    |
| 星辰铂金     | 6银50铜       | 16个    |
| 秘银锭       | 2银60铜       | 1个     |
| 精金锭       | 2银60铜       | 1个     |
| 山铜锭       | 2银60铜       | 1个     |
| 点金石锭     | 2银80铜       | 1个     |
| 钷锭         | 3银           | 1个     |
| 神圣锭       | 9银           | 1个     |
| 炼金锭       | 12银          | 1个     |
| 倚天锭       | 15银          | 1个     |

<div class="page-break"></div><br>

#### 农作物收购价格

| 物品名称 | 收购价格 | 数量 |
| -------- | -------- | ---- |
| 番茄     | 1银      | 64个 |
| 卷心菜   | 1银50铜  | 64个 |
| 洋葱     | 1银50铜  | 64个 |
| 稻米     | 2银      | 64个 |

### 2.2 出售

使用命令`/warp tp shop`前往「观畴园」商城，结束购买后可以使用`/back`返回原来的位置。

物品出售价格会根据服务器经济状况浮动，请以游戏内实际价格为准

#### 目前出售的商品类别

- 建筑材料

- 食品

- 药水等消耗品

!!! tip "Tips"

    如果遇到以上类别物品没有上架商店，可以喊小熊白菜去上架

#### 不会上架商店的商品类别

- 红石元件

- 彩灯

- 矿石（含原矿、粗矿、锭、合金锭、粗块、块等）

!!! warning "Warning"

    以上类别物品即使喊小熊白菜也一定不会被上架的

<div class="page-break"></div><br>

## 3 **自制模组说明**

!!! note "游玩建议"

    推荐的方式是跟随游戏内任务书的指引（按`L`打开任务书，按`F12`打开原版进度。很多模组的引导事实上已经包含在进度里面了，应当利用好这部分资源）

- 你需要点亮灯笼来使得一片区域变得稳定。当灯笼点亮时，经验条上方不会有圆形指示条，你也可以在四周看到粒子效果。
    - 请不要将点亮了的灯笼误认为是未点亮的灯笼——这条提示看起来很废话——但是真的有人会这样做。

## 4 **游戏特性**

为了游戏平衡性我们对原版特性做了微调，目标包括下列调整：

- 禁止了村民繁殖。

受添加的部分模组影响，服务器目前有以下已知特性：

- 女巫小屋结构无法正常生成新的女巫。因此，女巫刷怪塔无法正常使用。

## 5 **BUG 反馈途径**

!!! note "【Tencent Docs】棱镜树 Bug 反馈"

    <https://docs.qq.com/doc/DZHVnYmtydXN6RHFB>

不要只在群里说 bug（bug 有点小多小熊白菜记不住了x），建议填表的同时把复现方法和错误信息尽量发给小熊白菜。

---

<div class="page-break"></div><br>

## **附录 A：整合包常用快捷键及指令列表**

### **快捷键**

- minihud：`H+C`
- 投影模组：`X+C`
- FTB 任务书：`L`
- 原版进度：`F12`
- 望远镜：`F7`
- 语音聊天：`Enter`
- 语音聊天设置：`V`
- 其他快捷键可以通过按键绑定，或者从模组列表进入到模组设置中查看。

### **指令**

| 指令                      | 用途说明                                         |
| ------------------------- | ------------------------------------------------ |
| `/spawn`                  | 传送到出生点                                     |
| `/spawn set`              | 设置当前位置为出生点                             |
| `/tpa <目标玩家>`         | 请求传送到目标玩家身边                           |
| `/tpahere <目标玩家>`     | 请求目标玩家传送到你身边                         |
| `/tpaccept <目标玩家>`    | 接受传送请求                                     |
| `/tpdeny <目标玩家>`      | 拒绝传送请求                                     |
| `/home set <家名称>`      | 设置一个家（传送点）                             |
| `/home tp <家名称>`       | 传送到指定的家                                   |
| `/home delete <家名称>`   | 删除指定的家                                     |
| `/warp tp <传送点名称>`   | 传送到指定的公共传送点（中文的聚落暂时无法传送） |
| `/back`                   | 返回上一个位置                                   |
| `/randomteleport`或`/rtp` | 以`/spawn set`设置的点为中心，随机传送到世界某处 |

<div class="page-break"></div><br>

| 指令                      | 用途说明                                         |
| ------------------------- | ------------------------------------------------ |
| `/workbench`              | 打开工作台界面                                   |
| `/enderchest`             | 打开末影箱界面                                   |

## **附录 B：聚落说明**

### 原点城

- 位于梦境世界中心[0,0]的聚落。
- 悬浮在天空之上的华丽庄园。
- 聚落下方的陆地有大片枫叶林和薰衣草花海。

### 无名丘陵

- 玩家最多、占地最大的聚落！
- 你甚至可以看到手搓像素画）
- 大面积农田牲畜圈，不愁吃喝。
- 风格迥异（真的）、规划随意的众多建筑。

### 远苔岛

- 「旧名：曾经不欢迎联通的岛」
- 「这里似乎是一片废墟」
- 「孤悬在远海的深处」
- 「快跑！岛上的人呐喊着」
- （有小熊白菜的烂尾楼）

### 恩情半岛

- 拥有基础的生电设施，生产力较高。
- 最大的优点是位于各个聚落之间，去哪里都很方便。
- 风景不错的大型海岛，目前没有建筑，可开发地皮充裕。

## **附录 C：模组列表**

!!! note "服务器汉化说明"

    我们添加了一个汉化补丁，针对部分模组进行了汉化。如果你发现有某个模组的内容有较多未被汉化的，并且对游玩过程造成了困扰，可以在群里或[共享文档](https://docs.qq.com/doc/DZHVnYmtydXN6RHFB)中进行反馈。

<div class="page-break"></div><br>

### **额外游戏内容**

| Mod                        | 相关链接                                                  |
| -------------------------- | --------------------------------------------------------- |
| AdventureZ                 | [Wiki][AdventureZ_Wiki] / [MC百科][AdventureZ_MC百科]     |
| Alloy Forgery              | [Wiki][AlloyForgery_Wiki] / [MC百科][AlloyForgery_MC百科] |
| Biomes O' PLenty           | [MC百科][BiomesOPLenty_MC百科]                            |
| Bosses Of Mass Destruction | [MC百科][BossesOfMassDestruction_MC百科]                  |
| Farmer's Delight           | [MC百科][FarmersDelight_MC百科]                           |
| Kaleidoscope Cookery       | [MC百科][KaleidoscopeCookery_MC百科]                      |
| Lootr                      | [MC百科][Lootr_MC百科]                                    |
| Mythic Metals              | [Wiki][MythicMetals_Wiki] / [MC百科][MythicMetals_MC百科] |
| Numismatic Overhaul        | [MC百科][NumismaticOverhaul_MC百科]                       |
| Serene Seasons             | [MC百科][SereneSeasons_MC百科]                            |
| Starry Skies               | [MC百科][StarrySkies_MC百科]                              |

### **Hud 增强**

| Mod                | 相关链接                                                |
| ------------------ | ------------------------------------------------------- |
| AppleSkin          | [MC百科][AppleSkin_MC百科] / [GitHub][AppleSkin_GitHub] |
| BetterF3           | [GitHub][BetterF3_GitHub]                               |
| Colorful Subtitles | [GitHub][ColorfulSubtitles_GitHub]                      |
| MiniHUD            | [MC百科][MiniHUD_MC百科]                                |
| ModernUI           | [GitHub][ModernUI_GitHub]                               |
| Xaero's Minimap    | [MC百科][XaerosMinimap_MC百科]                          |
| Xaero's WorldMap   | [MC百科][XaerosWorldMap_MC百科]                         |

<div class="page-break"></div><br>

### **生活质量提升**

| Mod                     | 相关链接                               |
| ----------------------- | -------------------------------------- |
| Chat Heads              | [MC百科][ChatHeads_MC百科]             |
| CustomSkinLoader        | [GitHub][CustomSkinLoader_GitHub]      |
| Essential Commands      | [MC百科][EssentialCommands_MC百科]     |
| Inventory Profiles Next | [GitHub][InventoryProfilesNext_GitHub] |
| Iris                    | [GitHub][Iris_GitHub]                  |
| LambDynamicLights       | [GitHub][LambDynamicLights_GitHub]     |
| Litematica              | [GitHub][Litematica_GitHub]            |
| Just Zoom               | [MC百科][JustZoom_MC百科]              |
| Modmenu                 | [GitHub][Modmenu_GitHub]               |
| Neat                    | [GitHub][Neat_GitHub]                  |
| Presence Footsteps      | [GitHub][PresenceFootsteps_GitHub]     |
| Reactive Music          | [GitHub][ReactiveMusic_GitHub]         |
| Roughly Enough Items    | [GitHub][RoughlyEnoughItems_GitHub]    |
| Simple Voice Chat       | [Modrinth][SimpleVoiceChat_Modrinth]   |
| Sit                     | [GitHub][Sit_GitHub]                   |
| Spud's Shops            | [Modrinth][SpudsShops_Modrinth]        |
| Universal Shops         | [GitHub][UniversalShops_GitHub]        |
| Universal Graves        | [GitHub][UniversalGraves_GitHub]       |

### **游戏引导和教程**

<div class="page-break"></div><br>

| Mod          | 相关链接                      |
| ------------ | ----------------------------- |
| FTB Quests   | [GitHub][FTBQuests_GitHub]    |
| FTB Teams    | [GitHub][FTBTeams_GitHub]     |
| ModpackUtils | [MC百科][ModpackUtils_MC百科] |

### **性能优化**

| Mod                    | 相关链接                             |
| ---------------------- | ------------------------------------ |
| Continuity             | [GitHub][Continuity_GitHub]          |
| Reese's Sodium Options | [MC百科][ReesesSodiumOptions_MC百科] |
| Sodium                 | [GitHub][Sodium_GitHub]              |
| Sodium Extra           | [MC百科][SodiumExtra_MC百科]         |
| spark                  | [GitHub][spark_GitHub]               |
| ThreatenGL             | [GitHub][ThreatenGL_GitHub]          |
| Very Many Players      | [MC百科][VeryManyPlayers_MC百科]     |
| Lithium                | [MC百科][Lithium_MC百科]             |

### **API 及库依赖项**

| Mod                     | 相关链接                               |
| ----------------------- | -------------------------------------- |
| Architectury API        | [GitHub][ArchitecturyAPI_GitHub]       |
| Cardinal Components API | [GitHub][CardinalComponentsAPI_GitHub] |
| Cloth Config API        | [GitHub][ClothConfigAPI_GitHub]        |
| Fabric API              | [官网][FabricAPI_官网]                 |
| Fabric Language Kotlin  | [GitHub][FabricLanguageKotlin_GitHub]  |

<div class="page-break"></div><br>

| Mod                     | 相关链接                               |
| ----------------------- | -------------------------------------- |
| Forge Config API Port   | [GitHub][ForgeConfigAPIPort_GitHub]    |
| FTB Library             | [GitHub][FTBLibrary_GitHub]            |
| GeckoLib                | [GitHub][GeckoLib_GitHub]              |
| GlitchCore              | [GitHub][GlitchCore_GitHub]            |
| libIPN                  | [GitHub][libIPN_GitHub]                |
| MaLiLib                 | [GitHub][MasasLitemodLibrary_GitHub]   |
| owo-lib                 | [GitHub][owolib_GitHub]                |
| TerraBlender            | [GitHub][TerraBlender_GitHub]          |
| YetAnotherConfigLib     | [GitHub][YetAnotherConfigLib_GitHub]   |

### **自制模组**

| Mod              | 相关链接                         |
| ---------------- | -------------------------------- |
| Annoying Effects | [GitHub][AnnoyingEffects_GitHub] |
| Duel             | [Modrinth][Duel_Modrinth]        |
| Lantern In Storm | [GitHub][LanternInStorm_GitHub]  |
| Mirrortree       | [GitHub][Mirrortree_GitHub]      |
| Rewards          | [GitHub][Rewards_GitHub]         |
| Selling Bin      | [GitHub][SellingBin_GitHub]      |
| Sync Sign Notice | [GitHub][SyncSignNotice_GitHub]  |

### **服务器端**

#### **额外游戏内容（服务器端）**

<div class="page-break"></div><br>

| Mod                              | 相关链接                                    |
| -------------------------------- | ------------------------------------------- |
| Dungeons And Taverns             | [MC百科][DungeonsAndTaverns_MC百科]         |
| Moogs Voyager Structures         | [MC百科][MoogsVoyagerStructures_MC百科]     |
| Repurposed Structures            | [MC百科][RepurposedStructures_MC百科]       |
| Sky Villages                     | [MC百科][SkyVillages_MC百科]                |
| Structory                        | [MC百科][Structory_MC百科]                  |
| Towns And Towers                 | [MC百科][TownsAndTowers_MC百科]             |
| Terralith                        | [MC百科][Terralith_MC百科]                  |
| When Dungeons Arise              | [MC百科][WhenDungeonsArise_MC百科]          |
| When Dungeons Arise - Seven Seas | [MC百科][WhenDungeonsAriseSevenSeas_MC百科] |
| YUNG's Better End Island         | [MC百科][YUNGsBetterEndIsland_MC百科]       |
| YUNG's Better Mineshafts         | [MC百科][YUNGsBetterMineshafts_MC百科]      |
| YUNG's Better Ocean Monuments    | [MC百科][YUNGsBetterOceanMonuments_MC百科]  |
| YUNG's Better Strongholds        | [MC百科][YUNGsBetterStrongholds_MC百科]     |
| YUNG's Better Witch Huts         | [MC百科][YUNGsBetterWitchHuts_MC百科]       |
| YUNG's Bridges                   | [MC百科][YUNGsBridges_MC百科]               |
| YUNG's Extras                    | [MC百科][YUNGsExtras_MC百科]                |

#### **生活质量提升（服务器端）**

| Mod             | 相关链接                        |
| --------------- | ------------------------------- |
| Ageing Spawners | [MC百科][AgeingSpawners_MC百科] |

#### **API 及库依赖项（服务器端）**

<div class="page-break"></div><br>

| Mod          | 相关链接                     |
| ------------ | ---------------------------- |
| Cristel Lib  | [MC百科][CristelLib_MC百科]  |
| Midnight Lib | [MC百科][MidnightLib_MC百科] |
| YUNG's API   | [MC百科][YUNGsAPI_MC百科]    |

## **附录 D：棱镜树规范（第四版）**

!!! tips "省流版"

    🛑游戏内禁止：恶意PVP、偷家、辱骂、挑衅、阴阳怪气、强行造访、强行连接、强行赠送

    💬QQ群内禁止行为：违法违规、辱骂、威胁、人身攻击、开盒、带节奏、歪曲事实、煽动言论

    ⚖️执法方式：违规玩法将被抽查或举报处理，举报成功可挑选对方一件物品

本服为超困难生存类型服务器，在游戏前请仔细阅读[棱镜树梦境手册]，任务书[L键]将帮助您了解各种玩法，新人可在群里询问是否有老玩家愿意带（但将失去大量游戏体验）。

1. 本规范适用于棱镜树全体玩家。
2. 若被判罚玩家对判罚有异议，可申请其他运营组成员重审。
3. 若由服务器问题导致玩家墓碑丢失，需提交相应指南针向运营组申请理赔。
4. 若玩家发现运营组成员利用特权违反游戏规则，请公开举报，腐竹将严肃处理。
5. 本规范最终解释权归运营组(阁楼)所有。

### 服务器游玩规范细则

1. 恶意PVP：单方面战斗挑衅玩家、在PVP期间恶意破坏其他玩家重生点等。处罚封禁0.5-7天，屡次触犯最高可处罚永久封禁。
2. 偷家：未经同意（游戏聊天、社交软件、游戏内告示牌、书等）破坏玩家建筑、设施、景观，盗取或破坏玩家库存物品等。初犯处罚归还所有物品，复原破坏，公开赔礼道歉；再犯或拒绝接受处罚者封禁1-14天；屡次触犯最高可处罚永久封禁。
3. 言论过激：在游戏内（游戏聊天、游戏内告示牌、书等）辱骂、挑衅、屡次或过度阴阳玩家。初犯不公开处罚，仅处罚私下赔礼道歉；再犯处罚公开赔礼道歉；屡次触犯或拒绝处罚封禁1-3天；对玩家社群氛围破坏严重者最高处罚封禁14天。
4. 缺乏边界感：在玩家明确表示不接受造访、连接、赠予等合理游戏内行为时坚持实施上述行为。运营组可以出面调解，调解失败时由调解者灵活处罚，封顶不超过封禁3天。

<div class="page-break"></div><br>

### QQ社群规范细则

1. 违反法律法规或相关平台规范：灵活判罚，不设上限。
2. 不当言论：辱骂、威胁、人身攻击、未经同意（或事后谅解）的开盒等：初犯处罚公开赔礼道歉、尽可能消除负面影响，再犯处罚禁言不超过3天，屡次触犯或拒绝接受处罚者最高可移出QQ群并撤销游戏白名单。
3. 带节奏：发表煽动性言论或挑选证据拼凑传播歪曲事实等：处罚公开解释说明并赔礼道歉，拒绝接受处罚者最高可禁言7天，屡次触犯者最高可移出QQ群并撤销游戏白名单。

### 执法规范细则

1. 本部分实行随机抽检与玩家举报并行的巡查方案，仅对被发现的内容进行处理。
2. 欢迎大家互相监督举报，在运营组鉴定完毕后，举报者可以任选被举报者的一样私人物品拿走。

---

<br /><br /><br />

![合影](https://cos.bearcabbage.top/wp-content/uploads/2025/07/QQ图片20250730172435.jpeg)

<!-- 链接统一管理 -->
[AdventureZ_Wiki]: https://globox1997.github.io/wiki/mods/AdventureZ/
[AdventureZ_MC百科]: https://www.mcmod.cn/class/5052.html
[AlloyForgery_Wiki]: https://docs.wispforest.io/alloy-forgery/home/
[AlloyForgery_MC百科]: https://www.mcmod.cn/class/4958.html
[BiomesOPLenty_MC百科]: https://www.mcmod.cn/class/108.html
[BossesOfMassDestruction_MC百科]: https://www.mcmod.cn/class/4660.html
[FarmersDelight_MC百科]: https://www.mcmod.cn/class/2820.html
[MythicMetals_MC百科]: https://www.mcmod.cn/class/5297.html
[MythicMetals_Wiki]: https://wiki.mythicmetals.com/zh/
[SereneSeasons_MC百科]: https://www.mcmod.cn/class/1132.html
[Lootr_MC百科]: https://www.mcmod.cn/class/2924.html
[NumismaticOverhaul_MC百科]: https://www.mcmod.cn/class/9804.html
[AppleSkin_GitHub]: https://github.com/squeek502/AppleSkin
[AppleSkin_MC百科]: https://www.mcmod.cn/class/744.html
[BetterF3_GitHub]: https://github.com/TreyRuffy/BetterF3/
[ColorfulSubtitles_GitHub]: https://github.com/haykam821/Colorful-Subtitles
[MiniHUD_MC百科]: https://www.mcmod.cn/class/2311.html
[ModernUI_GitHub]: https://github.com/BloCamLimb/ModernUI-MC
[XaerosMinimap_MC百科]: https://www.mcmod.cn/class/1701.html
[XaerosWorldMap_MC百科]: https://www.mcmod.cn/class/1483.html
[ChatHeads_MC百科]: https://www.mcmod.cn/class/4523.html
[CustomSkinLoader_GitHub]: https://github.com/xfl03/MCCustomSkinLoader
[EssentialCommands_MC百科]: https://www.mcmod.cn/class/4493.html
[InventoryProfilesNext_GitHub]: https://github.com/blackd/Inventory-Profiles
[Iris_GitHub]: https://github.com/IrisShaders/Iris
[LambDynamicLights_GitHub]: https://github.com/LambdAurora/LambDynamicLights
[Litematica_GitHub]: https://github.com/maruohon/litematica
[JustZoom_MC百科]: https://www.mcmod.cn/class/5701.html
[Modmenu_GitHub]: https://github.com/TerraformersMC/ModMenu
[Neat_GitHub]: https://github.com/VazkiiMods/Neat
[PresenceFootsteps_GitHub]: https://github.com/Sollace/Presence-Footsteps
[ReactiveMusic_GitHub]: https://github.com/CircuitLord/ReactiveMusic
[RoughlyEnoughItems_GitHub]: https://github.com/shedaniel/RoughlyEnoughItems
[SimpleVoiceChat_Modrinth]: https://modrinth.com/plugin/simple-voice-chat
[Sit_GitHub]: https://github.com/bl4ckscor3/Sit
[SpudsShops_Modrinth]: https://modrinth.com/mod/spuds-shops
[UniversalShops_GitHub]: https://github.com/Patbox/UniversalShops
[UniversalGraves_GitHub]: https://github.com/Patbox/UniversalGraves
[FTBQuests_GitHub]: https://github.com/FTBTeam/FTB-Quests
[FTBTeams_GitHub]: https://github.com/FTBTeam/FTB-Teams/
[ModpackUtils_MC百科]: https://www.mcmod.cn/class/17151.html
[Continuity_GitHub]: https://github.com/PepperCode1/Continuity
[ReesesSodiumOptions_MC百科]: https://www.mcmod.cn/class/4905.html
[Sodium_GitHub]: https://github.com/CaffeineMC/sodium
[SodiumExtra_MC百科]: https://www.mcmod.cn/class/3701.html
[spark_GitHub]: https://github.com/lucko/spark
[ThreatenGL_GitHub]: https://github.com/Numelon-Softworks/ThreatenGL
[VeryManyPlayers_MC百科]: https://www.mcmod.cn/class/6473.html
[Lithium_MC百科]: https://www.mcmod.cn/class/2292.html
[ArchitecturyAPI_GitHub]: https://github.com/architectury/architectury-api
[CardinalComponentsAPI_GitHub]: https://github.com/Ladysnake/Cardinal-Components-API
[ClothConfigAPI_GitHub]: https://github.com/shedaniel/cloth-config
[FabricAPI_官网]: https://fabricmc.net/
[FabricLanguageKotlin_GitHub]: https://github.com/FabricMC/fabric-language-kotlin/
[ForgeConfigAPIPort_GitHub]: https://github.com/Fuzss/forgeconfigapiport
[FTBLibrary_GitHub]: https://github.com/FTBTeam/FTB-Library
[GeckoLib_GitHub]: https://github.com/bernie-g/geckolib
[GlitchCore_GitHub]: https://github.com/Glitchfiend/GlitchCore
[libIPN_GitHub]: https://github.com/blackd/libIPN
[MasasLitemodLibrary_GitHub]: https://github.com/maruohon/malilib
[owolib_GitHub]: https://github.com/wisp-forest/owo-lib
[TerraBlender_GitHub]: https://github.com/Glitchfiend/TerraBlender
[YetAnotherConfigLib_GitHub]: https://github.com/isXander/YetAnotherConfigLib
[AnnoyingEffects_GitHub]: https://github.com/MirrorTree-MC/AnnoyingEffects
[Duel_Modrinth]: https://modrinth.com/mod/duel-mod
[LanternInStorm_GitHub]: https://github.com/MirrorTree-MC/Lantern-in-Storm
[Mirrortree_GitHub]: https://github.com/MirrorTree-MC/MirrorTree-Journey
[SellingBin_GitHub]: https://github.com/MirrorTree-MC
[Rewards_GitHub]: https://github.com/MirrorTree-MC
[SyncSignNotice_GitHub]: https://github.com/MirrorTree-MC
[DungeonsAndTaverns_MC百科]: https://www.mcmod.cn/class/10835.html
[MoogsVoyagerStructures_MC百科]: https://www.mcmod.cn/class/8583.html
[RepurposedStructures_MC百科]: https://www.mcmod.cn/class/4518.html
[SkyVillages_MC百科]: https://www.mcmod.cn/class/5142.html
[Structory_MC百科]: https://www.mcmod.cn/class/6793.html
[TownsAndTowers_MC百科]: https://www.mcmod.cn/class/7000.html
[Terralith_MC百科]: https://www.mcmod.cn/class/4557.html
[WhenDungeonsArise_MC百科]: https://www.mcmod.cn/class/3607.html
[WhenDungeonsAriseSevenSeas_MC百科]: https://www.mcmod.cn/class/13131.html
[YUNGsBetterEndIsland_MC百科]: https://www.mcmod.cn/class/12175.html
[YUNGsBetterMineshafts_MC百科]: https://www.mcmod.cn/class/2788.html
[YUNGsBetterOceanMonuments_MC百科]: https://www.mcmod.cn/class/7904.html
[YUNGsBetterStrongholds_MC百科]: https://www.mcmod.cn/class/3787.html
[YUNGsBetterWitchHuts_MC百科]: https://www.mcmod.cn/class/6618.html
[YUNGsBridges_MC百科]: https://www.mcmod.cn/class/5031.html
[YUNGsExtras_MC百科]: https://www.mcmod.cn/class/4276.html
[AgeingSpawners_MC百科]: https://www.mcmod.cn/class/5539.html
[CristelLib_MC百科]: https://www.mcmod.cn/class/12373.html
[MidnightLib_MC百科]: https://www.mcmod.cn/class/6776.html
[YUNGsAPI_MC百科]: https://www.mcmod.cn/class/3372.html
[StarrySkies_MC百科]: https://www.mcmod.cn/class/6922.html
[KaleidoscopeCookery_MC百科]: https://www.mcmod.cn/class/20850.html
