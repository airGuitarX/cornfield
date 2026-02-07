---
title: 2025 找工总结
author: [RR]
description: 去年11月左右全组人都跑光了，关系很好的同事要么离职要么转组，原组直接解散让我萌生了跑路的想法，加上公司准备从2025年开始RTO5，更不想呆了。被动并入姐妹组之后发现oncall十分阴间，于是立刻决定年底开始刷题，在经济下行时毅然加入了找工大军……
slug: 2025-job-hunting-summary
date: 2025-10-06 00:00:00+0000
categories:
    - 工作
tags:
    - jobhunting
    - leetcode
    - system design
weight: 1       # You can add weight to some posts to override the default sorting (date descending)
---

## 找工时间线与整体总结

我： 8yoe, general SDE

去年11月左右全组人都跑光了，关系很好的同事要么离职要么转组，原组直接解散让我萌生了跑路的想法，加上公司准备从2025年开始RTO5，更不想呆了。被动并入姐妹组之后发现oncall十分阴间，于是立刻决定年底开始刷题。

我的找工目标：title平级/升级 + base pay持平/增加 + RTO天数更少的任何公司，雇员人数>100。

面试准备应该是找工中整体最花时间的，1-4月，7-8月都在刷题和准备SD+BQ，中间5月回家了一趟参加CP导致整体进度拉长（不应该啊不应该可是那是CP啊！），于是就一直找到了9月。4月收了一些面试，也有一家走完了全部终面流程，但直接被Ghost没有下文了。这家因为和国内有业务所以明确说明有些时候需要晚上开会，本来也不是很想去也就没有继续follow up。

6月-7月回来继续刷题，从Java换成了Python基本等于从0开始，但是还是强烈建议每一个用C++/Java的人换成Python，Python大法好！语法简单，build-in function多省时又省力。

8月又修了一版简历开始狂投，收了几个面试最后拿到了一个full remote offer，本着绝不为难自己的想法直接从了。

转化率如下：
<img src="flow.png" alt="converting-flow">

## 准备什么，怎么准备

以下内容全部为网上免费资料，SDE找工是一个被创造出来的需求，我的目标是在不牺牲ROI的情况下，能不花钱做成的事绝对不花钱。当然不是说不能花钱，根据自己的需要衡量就好。

### 简历
首先repact after me：

1. 绝对！不要！用2 column 板式！影响ATS识别。
2. 10 yoe 以下一律1页解决，除非你有专利。

Reddit找的实用参考： https://www.reddit.com/r/EngineeringResumes/wiki/index/ 

内容上：
1. 杜绝没用的副词 = greatly, significently, etc.
2. 有数据一定要列数据 =  improve cache hit rate by x%, saving 2 hours on deployment, event reached out to 10k people, etc.
3. 有工作经验学校就写最后

### 刷题 - LeetCode + NeetCode
先去看一遍常见DSA，这里推荐Hellow Interview的Code 部分： https://www.hellointerview.com/learn/code

AlgoMonster也可以看一下，不过这个最好结合做题： https://algo.monster/dashboard AlgoMonster在DSA部分就涉及到付费，不过我没有买，打算看完免费内容不够再说（实际上完全够用）。

接下来 LeetCode 150 或者 NeetCode 150刷就完事，看到Hard直接跳过，性价比太低。AlgoMonster的flow chart很有用： https://algo.monster/flowchart 类似于一个决策树帮你快速定位某道题应该用什么技巧解决。

LC不懂的问题可以看 AlgoMonster的解法 https://algo.monster/liteproblems/100 ，或者有请ChatGPT老师。碰到做不出来/没有思路的题我会直接看答案，然后在Note里总结下我流思考步骤/解题要点，为二刷三刷节省时间，LC的Note页面很方便可以看所有的note： https://leetcode.com/notes/


### 系统设计 

#### High Level Design

Hello Interview- System Design in a Hurry: https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction

目前觉得最有用的网站，建议是把免费部分全看完再决定要不要买付费内容。我没买因为感觉够用了。


另外推荐两本已经被推荐烂了的书：
1. [System Design Interview - An Insider's Guide(Alex Xu)](https://bytes.usc.edu/~saty/courses/docs/data/SystemDesignInterview.pdf)
2. [Designing Data-Intensive Applications, 2nd Edition](https://github.com/Vonng/ddia) 

都推荐读英文版。适合从0开始读学习SD且有一定时间的人，没有时间/只为了找工作就看Hello Interview吧。顺序上我会比较推荐DDIA开始，SD Interview讲的内容比较简单忽略了一些Deep Dive，个人觉得用DDIA打基础的话，读SD Interview会更轻松。
 
#### Low Level Design

没准备太多，实际上也只有一家公司考了，姑且放一份参考资料：[awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources?tab=readme-ov-file)

### Behavioral Questions

推荐2个网站： 
1. [Mastering Behavioral Interviews](https://thebehavioral.substack.com/p/roadmap-to-behavioral-interview-prep) 主要针对BQ该准备什么和如何取舍
2. [Tech Interview Handbook](https://www.techinterviewhandbook.org/behavioral-interview-questions/) 综合类如何准备面试，但也有专门的BQ section,面试最后不知道问HR/Manager/SDE/Leadership 什么问题可以从这里找

根据从小地瓜上学来的经验，BQ问题万变不离其宗就是这10条的变体：

1. teamwork 
1. leadership
1. motivation
1. challenge
1. conflict
1. learn new skills
1. multitasking
1. planning
1. client service
1. failure


## 然后呢？

练……虽然我不推荐投入全部个人时间找工（那样很快就会崩溃），但是每天划出一段雷打不动的时间刷题/看书/练习BQ还是很有必要的，一旦度过最初的启动阶段心情会好很多。希望大家都能在这个糟糕的市场中成功打捞一份工作！

