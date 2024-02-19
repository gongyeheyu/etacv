# etaCV

![](https://badgen.net/badge/state/sleep/yellow)
![](https://badgen.net/badge/Designer/GONGYE%20Heyu/blue)
![](https://badgen.net/badge/code/etaCV/blue)

**本项目已于2023年3月5日进入无限期休眠，我们等待着这颗种子发光。**

#由于本项目的文档即本README极不完善，部分语义仍在修改。因此恳请各位大佬帮忙，谢谢。  

#本项目的开发大致以实用为目的：有需要->写文档（也有可能不写）->写代码  

#本项目的开发采用了业界领先的TreeNewBee-Driven Development方式。具体地说，就是每个功能都是先把文案写好（也有可能写不好），直接牛皮就吹起来了，然后根据牛皮写代码，最后再实现功能让牛皮不被吹破。 这样做有两大好处：第一不值得"TreeNewBee"的功能一概没有。第二确保了每个功能都有文案负责吹嘘（也有可能没有）  

## 1.简介

etaCV是一种以简单，易用，快速，准确为代表的强类型，面向对象的解释型语言。旨在快速构建应用和帮助初学者快速理解编程。它被设计用于脚本，简易程序。  

etaCV的设计简单明了。它使用简单的语法，并且被设计为易于阅读和理解。etaCV还具有广泛的内置库和函数，使编程更容易。

```特性  
它的特性有： 
    强类型，面向对象  
    惰性求值  
    静态类型  
    函数结果可能受外界影响  
    初学者易上手，对非程序员友好  
    简单且严格的语法  
    需要考虑垃圾回收  
    可以与其他语言相互调用  
    缺少分号  
    有较为严格的语言规范  
    程序有可扩展性  
    大量且易用的API  
    同时存在解释器和编译器  
    没有“类”的概念  
```

## 1.第一个实例程序  

```example
#this is a example  
print "hello,world!"  
```

首先我们看到了第一行文字：这是一段注释，etaCV有两种注释：  

```comment
#这是单行注释  
/*这是  
多行注释*/  
```  

再来看第二行文字：print是一个输出关键字，引号内为要输出的内容。  

## 2.变量  

下面看一个例子  

```example
int year = 2022  
```

这个例子使用int关键字声明一个名为year的整数变量并给它赋值为"2022"  
变量名可以为英文字母，数字，汉字，下划线组成，但不能以数字开头。  
并且，etaCV对关键字，变量名，文件名大小写不敏感，`int`,`Int`,`INT`在etaCV中是同一个东西。  

## 3.数据类型  

现在我们来看一下数据类型相关内容  
我们来看一个例子  

```example  
int y = 2022  
int m = 11  
print y + m  
```  

它将会有如下输出：

```print
202211 
```

etaCV有四种数据类型：  

```type
int 整数  
flo 浮点数  
str 字符串  
boo 布尔值  
```

int型变量用于存储整数，只要内存足够，可以容纳无限大(小)的数值。  
flo型变量用于存储浮点数，可以容纳无限大(小)的数值。  
str型变量用于存储字符串，字符串可以包含任何字符。  
boo型变量用于存储布尔值，布尔值只有两个值：true和false，是 int 的子类。  

```type
bool(0)     # => False
bool(1)     # => True
```

如果你不知道一个变量是什么类型，可以通过type()函数来检验  

```type
print ecv:type(year)  
```

如你所见，不同类型的变量可以以字符串形式连接  

### 3.1不同数据类型的互相转换  

etaCV中数据类型的转换很简单，如果要将year变量转换为字符串，只需要如下操作  

```str
ecv:str(year)  
```

转换为int型，布尔型返回为0或1，浮点数返回整数部分，字符串返回null  
转换为float型，布尔型返回为0或1，字符串返回null  
转换为str型，布尔型返回为true或flase  
转换为boo型，int或float为1时返回1，其余均返回0  

## 4.列表
```list
#生成列表
int li1 = []    # => []
int li2 = [4, 5, 6]     # => [4, 5, 6]
int li3 = ecv:list((1, 2, 3))   # => [1, 2, 3]
int li4 = list(range(1, 11))
# => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#添加元素
int li = []
li.append(1)    # => [1]
li.append(2)    # => [1, 2]
li.append(4)    # => [1, 2, 4]
li.append(3)    # => [1, 2, 4, 3]

#删除元素
li.del(2)    # => [1, 4, 3]

#修改元素
li[0] = 10    # => [10, 4, 3]

#切片
a_list[start:end]
a_list[start:end:step]
li[1:3]    # => [4, 3]
li[1:3:2]    # => [4]
li[::2]    # => [1, 3]
li[::-1]    # => [3, 4, 2, 1]

#列表长度
ecv:len(li)    # => 4

#连接
int li = [1, 2, 3]
int li2 = [4, 5, 6]
li + li2    # => [1, 2, 3, 4, 5, 6]

#判断元素是否在列表中
1 in li    # => true
2 in li    # => true
0 in li    # => false
```

## 6.判断
```if
int number = int(ecv:input('输入一个整数：'))
if (number < 0) {
    print "您输入了一个负数。"
} else {
    print "您输入了一个非负整数。"
}
```

## 4.字符串的分片与索引  

字符串可以通过cut()来进行分片和索引  
下面举几个例子：  

```example
str a = abcdefgh  
print a.ecv:list(0)  
print a.ecv:list(-7)  
print a.ecv:list(7)  
print a.ecv:list(-0)  
print a.ecv:list(0:2)  
print a.ecv:list(:2)  
print a.ecv:list()  
```

输出：

```print
a  
a  
h  
h  
a, b, c  
a, b, c  
a, b, c, d, e, f, g, h  
```

如你所见，和其他语言一样，在第四行中，从第0个字符开始到第二个字符，但不包含第二个  

## 5.函数和关键字  

总之，函数就是一个输入某个东西就能输出某个东西的东西  
与其他语言一样，etaCV有一些内建函数，向它们输入数据，都会得到一个返回值。  
下面的例子定义了一个函数  

```example
fun local:f2c(c)   
    int f = (c * 9/5 + 32)  
    return f + "˚F"  
print f2c(35)
```
  
返回：

```re
95 ˚F
```

第一行def关键字表示定义（或声明）一个名为f2c（）的函数，并且这个函数返回一个int型数据

```others
关键字:var print input if else return def fun sleep continue break int float string bool null none true flase local ecv

运算符:+ - * / ^(乘方) %(取模) == != < > <= >=

内建函数：  
input()返回输入信息
int()返回输入数据的整数形式（布尔型返回为0或1，浮点数返回整数部分，字符串返回null(即空集)）
float()返回输入数据的浮点数形式（布尔型返回为0或1，字符串返回null）
str()返回输入数据的字符串形式（布尔型返回为true或flase）
bool()返回输入数据的正误
list()返回输入数据的集合或分片集合
hash()返回输入数据的哈希值
len()返回输入数据的长度
ramdom()返回随机数

保留字：  
var print input if else return def fun sleep continue break int float string bool null none true flase local ecv moloc  
```
