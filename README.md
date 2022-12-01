# etacv

## 1.第一个实例程序  

```example
//this is a example  
output (hello,world!)  
```

首先我们看到了第一行文字：这是一段注释，etaCV有两种注释：  

```comment
//这是单行注释  
#这是  
多行注释#  
```  

再来看第二行文字：output()是一个输出函数，括号内为要输出的内容。  

## 2.变量  

下面看一个例子  

```example
int year = 2022  
```

这个例子使用int关键字声明一个名为year的整数变量并给它赋值为"2022"  
变量名可以为英文字母，数字，汉字，下划线组成，但不能以数字开头。  
并且，etaCV对关键字，变量名大小写敏感，`int`,`Int`,`INT`并不是同一个东西，但对文件名大小写不敏感。  

## 3.数据类型  

现在我们来看一下数据类型相关内容  
我们来看一个例子  

```example  
int y = 2022  
str m = 11  
output ($y + $m)  
```  

它将会有如下输出：

```output
202211 
```

etaCV有四种数据类型：  

```type
int 整数  
float 浮点数  
string 字符串  
bool 布尔值  
```

如果你不知道一个变量是什么类型，可以通过type()函数来检验  

```type
output type($year)  
```

如你所见，不同类型的变量可以以字符串形式连接  

### 3.1不同数据类型的互相转换  

etaCV中数据类型的转换很简单，如果要将year变量转换为字符串，只需要如下操作  

```str
string $year  
```

转换为int型，布尔型返回为0或1，浮点数返回整数部分，字符串返回null  
转换为float型，布尔型返回为0或1，字符串返回null  
转换为str型，布尔型返回为true或flase  
转换为bool型，int或float为1时返回1，其余均返回0  

## 4.字符串的分片与索引  

字符串可以通过cut()来进行分片和索引  
下面举几个例子：  

```example
string a = abcdefgh  
output ($a.list(0))  
output ($a.list(-7))  
output ($a.list(7))  
output ($a.list(-0))  
output ($a.list(0:2))  
output ($a.list(:2))  
output ($a.list())  
```

输出：

```output
a  
a  
h  
h  
a,b,c  
a,b,c  
a,b,c,d,e,f,g,h  
```

如你所见，和其他语言一样，在第四行中，从第0个字符开始到第二个字符，但不包含第二个  

## 5.函数和关键字  

总之，函数就是一个输入某个东西就能输出某个东西的东西  
与其他语言一样，etaCV有一些内建函数，向它们输入数据，都会得到一个返回值。  
下面的例子定义了一个函数  

```example
define int f2c(c)   
    int f = (c * 9/5 + 32)  
    return f + "˚F"  
output f2c(35)
```
  
返回：

```re
95 ˚F
```

第一行def关键字表示定义（或声明）一个名为f2c（）的函数，并且这个函数返回一个int型数据

```others
关键字:var if else return define sleep continue break int float string bool null none true flase
运算符:+ - * / ^(乘方) %(取模) == != < > <= >=
input()返回输入信息
output()返回输出内容  
int()返回输入数据的整数形式（布尔型返回为0或1，浮点数返回整数部分，字符串返回null(即空集)）
float()返回输入数据的浮点数形式（布尔型返回为0或1，字符串返回null）
str()返回输入数据的字符串形式（布尔型返回为true或flase）
bool()返回输入数据的正误
list()返回输入数据的集合或分片集合
hash()返回输入数据的哈希值
len()返回输入数据的长度
ramdom()返回随机数
```
