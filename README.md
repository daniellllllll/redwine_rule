**ABOUT**

此project為使用UC Irvine Machine Learning Repository網站中所提供的Wine Data Set資料，連結如下：

http://archive.ics.uci.edu/ml/datasets/Wine


此研究希望利用紅酒的參數與資料找出一套規則，以判斷出高品質的紅酒組成成分

所使用方法為Decision tree的CART，由於CART為二元數，所以將不同品質的紅酒再分成兩類

區分方法為將所以資料依照不同品質畫出直方圖，在此將品質7和8分類為一類，其餘分類成第二類
![image](https://github.com/daniellllllll/redwine_rule/blob/master/hiostogram.png)
                                    fig.1

![image](https://github.com/daniellllllll/redwine_rule/blob/master/wine-1.png)

Confusion matrix

![image](https://github.com/daniellllllll/redwine_rule/blob/master/cm.png)

CART演算法套件使用python的scikit-learn

在程式最後參考http://xccds1977.blogspot.tw/2014/10/python_26.html

用RandomForest跑一次該筆資料，並與CART比較成效
 
希望大家參考看看，並給予指導 ＾＿＾
