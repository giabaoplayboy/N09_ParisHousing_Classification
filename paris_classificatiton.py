# -*- coding: utf-8 -*-
"""Paris_Classificatiton.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/192eJy2RJF4Och43h0g668teuGgzD57KC

#PHÂN LOẠI NHÀ Ở PARIS (PHÁP)

#Thư viện Python
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_predict, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, plot_confusion_matrix, roc_curve

"""#Đọc và phân tích dữ liệu


"""

df = pd.read_csv("/content/ParisHousingClass.csv")

#hiển thị 10 dòng đầu tiên
df.head(10)

#hiển thị các thông tin mỗi cột
df.info()

"""**Đếm các dòng dữ liệu của thuộc tính**


"""

dict = {}
for i in list(df.columns):
  dict[i] = df[i].value_counts().shape[0]

pd.DataFrame(dict , index=['count']).transpose()

# Shuffle the data
# Trộn dữ liệu
from sklearn.utils import shuffle
df = shuffle(df)
df = df.reset_index(drop=True)

#hiển thị 10.000 dòng dữ liệu gốc và 18 thuộc tính
print("Dữ liệu gốc và thuộc tính:", df.shape)

#Xem classification
df['category'].value_counts()

"""#Liệt kê các thuộc tính

Nhận xét:


1.   Lớp Basic có 8735 dòng dữ liệu
2.   Lớp luxury có 1265 dòng dữ liệu
"""

#đếm số lượng nhà basic and luxury
sns.countplot( x = df['category'])
# fig.savefig('report_category.png')

"""Tập dữ liệu của thuộc tính Category này bao gôm hai lớp Basic và Luxury này không cân bằng"""

round(df['category'].value_counts()/df.shape[0]*100,2).plot.pie(autopct = '%1.1f%%', colors = ['lightcoral', 'pink'])
# fig.savefig('report_category_circle.png')

"""Biểu đố thể hiện phần trăm, cho thấy rõ thuộc tính không cân bằng"""

#đếm số lượng nhà basic and luxury
plt.figure(figsize=(30, 18))
sns.countplot( x = df['numberOfRooms'])
# fig.savefig('report_numberOfRooms.png')

#hiển thị 10 dòng dữ liệu đầu tiên
df.head(10)

df.info()

df.duplicated().sum()

"""Dữ liệu không bị trùng lặp"""

#Hiển thị thuộc tính các cột trong data
df.columns

#Visualize mô hình đếm sân vườn 
count = df['hasYard'].value_counts()
sns.set_context(font_scale=1.5)
plt.figure(figsize=(6,5))
sns.barplot(count.index, count.values, alpha=0.6, palette="prism")
plt.ylabel('Count', fontsize=12)
plt.xlabel('Has Yard', fontsize=12)
plt.title('Yes / No')
plt.show()
# fig.savefig('report_hasYard.png')

sns.countplot(x = df["hasYard"], hue=df["category"],palette="rocket")
# fig.savefig('report_hasYard_category.png')

#Chúng tôi lưu ý rằng tất cả các căn hộ sang trọng phải có sân, nhưng không phải tất cả các căn hộ có sân là sang trọng
pd.crosstab(df['category'], df['hasYard'], margins=True).style.background_gradient(cmap="PuBuGn")

#Visualize mô hình đếm hồ bơi
count = df['hasPool'].value_counts()
sns.set_context(font_scale=1.5)
plt.figure(figsize=(6,5))
sns.barplot(count.index, count.values, alpha=0.6, palette="prism")
plt.ylabel('Count', fontsize=12)
plt.xlabel('Has Pool', fontsize=12)
plt.title('Yes / No')
plt.show()
# fig.savefig('report_hasPool.png')

sns.countplot(x = df["hasPool"], hue=df["category"],palette="rocket")
# fig.savefig('report_hasPool_category.png')

#Chúng tôi lưu ý rằng tất cả các căn hộ sang trọng đều phải có hồ bơi, nhưng không phải tất cả các căn hộ có hồ bơi đều sang trọng
pd.crosstab(df['category'], df['hasPool'], margins=True).style.background_gradient(cmap="PuBuGn")

plt.figure(figsize=(30,15))
sns.countplot(x = df["floors"], hue=df["category"],palette="rocket")
# fig.savefig('report_floors.png')

#Visualize mô hình số vùng lân cận
count = df['cityPartRange'].value_counts()
sns.set_context(font_scale=1.5)
plt.figure(figsize=(6,5))
sns.barplot(count.index, count.values, alpha=0.6, palette="prism")
plt.ylabel('Count', fontsize=12)
plt.xlabel('City Part Range', fontsize=12)
plt.show()
# fig.savefig('report_cityPartRange.png')

plt.figure(figsize=(20,10))
sns.countplot(x = df["cityPartRange"], hue=df["category"],palette="rocket")
# fig.savefig('report_cityPartRange_category.png')

pd.crosstab(df['category'], df['cityPartRange'], margins=True).style.background_gradient(cmap="PuBuGn")

#Visualize mô hình số lượng chủ sở hữu
count = df['numPrevOwners'].value_counts()
sns.set_context(font_scale=1.5)
plt.figure(figsize=(6,5))
sns.barplot(count.index, count.values, alpha=0.6, palette="prism")
plt.ylabel('Count', fontsize=12)
plt.xlabel('Number PrevOwners', fontsize=12)
plt.show()
# fig.savefig('report_numPrevOwners.png')

plt.figure(figsize=(20,10))
sns.countplot(x = df["numPrevOwners"], hue=df["category"],palette="rocket")
# fig.savefig('report_numPrevOwners_category.png')

pd.crosstab(df['category'], df['numPrevOwners'], margins=True).style.background_gradient(cmap="PuBuGn")

plt.figure(figsize=(20,16))
sns.set_theme(style="whitegrid")
sns.color_palette("husl", 9)
sns.countplot(df['made'])
plt.xticks(rotation=90)
plt.show()
# fig.savefig('report_made.png')

plt.figure(figsize=(30,15))
sns.countplot(x = df["made"], hue=df["category"],palette="rocket")
# fig.savefig('report_made_category.png')

pd.crosstab(df['category'], df['made'], margins=True).style.background_gradient(cmap="PuBuGn")

plt.figure(figsize=(10,8))
sns.countplot(x = df["hasStorageRoom"], hue=df["category"],palette="rocket")
# fig.savefig('report_hasStorageRoom_category.png')

plt.figure(figsize=(20,15))
sns.countplot(x = df["hasGuestRoom"], hue=df["category"],palette="rocket")
# fig.savefig('report_hasGuestRoom_category.png')

df.hist(bins = 50, figsize = (20,20))
plt.show()
# fig.savefig('report_all.png')

#Giá cả và mét vuông phụ thuộc vào nhau
plt.figure(figsize=(16, 12))
sns.distplot(df.squareMeters, bins = 45, color = '#f88f01', hist = True)
plt.xlabel(' Price of Houses in a block in $', fontsize=16)
plt.ylabel('square meter', fontsize=16)
plt.title('Average Distribution of Median Price of Housing in a Block', fontsize=20)
plt.show()
# fig.savefig('report_price_squaremeter.png')

plt.figure(figsize=(20,12))
sns.heatmap(df.corr(), cbar = True,annot = True, cmap='RdPu', linewidths=1, linecolor='black')
# fig.savefig('heatmap_1.png')

#Mối quan hệ giữa năm thực hiện và giá cả cho cả hai loại
plt.figure(figsize=(16, 12))
sns.lineplot(x = df["made"], y = df["price"] , hue = df["category"])
# fig.savefig('report_price_made.png')

#Biến đổi chữ thành số của thuộc tính caterogy
df['category'].replace("Basic", 0 , inplace = True)
df['category'].replace("Luxury", 1 , inplace = True)

#xem lại dữ liệu sau khi mã hóa
df.describe()

df.head(10)

#Kiểm tra giá so với mét vuông
#a
df['price']/df['squareMeters']
#vì vậy sẽ xóa thuộc tính mét vuông hoặc giá cả

plt.figure(figsize=(20,12))
sns.heatmap(df.corr(), cbar = True,annot = True, cmap='RdPu', linewidths=1, linecolor='black')
# fig.savefig('heatmap_1.png')

#Sẽ chọn giá để xóa
df = df.drop(["price"], axis = 1)

df.info()
#Sau khi xóa xong thuộc tính price, sẽ còn lại 17 thuộc tính trong tập dữ liệu

#Kiểm tra ngoại lệ không
# Hầu như không có ngoại lệ, ngoại trừ trong category
# vì căn hộ sang trọng chiếm thiểu số (khoảng 12,6%)
df.plot(kind = "box" , subplots = True , figsize = (18,18) ,  layout = (6,3))
plt.show()
# fig.savefig('report_all_1.png')

"""Lấy mẫu dữ liệu để ngang bằng với hàng luxury"""

luxury = df[df['category']==1]
luxury
#lấy tất cả hàng luxury

luxury.shape
#Hàng luxury có 1265 dòng dữ liệu và 17 thuộc tính

basic = df[df['category']==0].sample(1265)
basic
#Lấy hàng basic ngang bằng với dòng dữ liệu luxury là 1265 để tiến hành train data và test data

"""Nhận xét: Có một mối tương quan lớn giữa giá và mét vuông. vì vậy, chúng tôi quyết định bỏ squareMeter để áp dụng mô hình"""

#Xóa SquareMeters 
df.drop(['squareMeters'], axis=1, inplace =True)
df

"""#Models"""

X =df.drop(['category'], axis = 1).values
y = df['category'].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)

X_test = sc.transform(X_test)

"""#Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth = 5, max_features= 7)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)

from sklearn import tree
from sklearn.metrics import confusion_matrix
fig = plt.figure(figsize = (20,20))
tree.plot_tree(dt , filled = True)
# fig.savefig('decesion_tree.png')

#Visualize biểu đồ thể hiện các đặc tính quan trọng trong bộ dữ liệu Paris Housing
def f_importances(coef, names, top=-1):
    imp = coef
    imp, names = zip(*sorted(list(zip(imp, names))))

    if top == -1:
        top = len(names)

    plt.barh(range(top), imp[::-1][0:top], align='center')
    plt.yticks(range(top), names[::-1][0:top])
    plt.title('feature importances')
    plt.show()

features_names = ['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'floors',
       'cityCode', 'cityPartRange', 'numPrevOwners', 'made', 'isNewBuilt',
       'hasStormProtector', 'basement', 'attic', 'garage', 'hasStorageRoom',
       'hasGuestRoom', 'price']

f_importances(abs(dt.feature_importances_), features_names, top=12)

print('TEST RESULT:\n ')
# REPORT
print('Decision tree Classifier Report:\n\n{} \n' .format(classification_report(y_test, dt_pred)))

res = cross_val_score(dt, X_test, y_test, cv=10, n_jobs=1, scoring = 'accuracy')

#Độ chính xác trung bình
print('Average Accucy: \t{0:.4f}\n'.format((res.mean())))

print('Standard Deviation: \t{0:.4f}\n'.format((res.std())))

print('Confusion Matrix :\n{}\n'.format(confusion_matrix(y_test, dt.predict(X_test))))

print('Accuracy Score :\t\t{}%'.format(round(dt.score( X_test, y_test)*100,2)))

plot_confusion_matrix(dt, X_test, y_test)
# fig.savefig('matrix_dt.png')

"""#RANDOM FOREST"""

from sklearn.ensemble import RandomForestClassifier as RF
rf = RF(n_estimators = 50, criterion = 'entropy', random_state = 42)
rf.fit(X_train , y_train)

rf_pred = rf.predict(X_test)

print('TEST RESULT:\n ')
# REPORT
print('Random Forest Classifier report:\n\n{} \n' .format(classification_report(y_test, rf_pred)))

res = cross_val_score(rf, X_test, y_test, cv=10, n_jobs=1, scoring = 'accuracy')

#Độ chính xác trung bình
print('Average Accucy: \t{0:.4f}\n'.format((res.mean())))

print('Standard Deviation: \t{0:.4f}\n'.format((res.std())))

print('Confusion Matrix :\n{}\n'.format(confusion_matrix(y_test, rf.predict(X_test))))

print('Accuracy Score :\t\t{}%'.format(round(rf.score( X_test, y_test)*100,2)))

plot_confusion_matrix(rf, X_test, y_test)
# fig.savefig('matrix_rf.png')

print ('Train Accuracy - : {}%'.format(round(rf.score( X_train, y_train)*100,2)))
print ('Test Accuracy - : {}%'.format(round(rf.score( X_test, y_test)*100,2)))

"""#K-Nearest Neighbors"""

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

kn_pred = knn.predict(X_test)

from sklearn.model_selection import cross_val_predict, cross_val_score
print('TEST RESULT:\n ')
# REPORT
print(classification_report(y_test, kn_pred))

res = cross_val_score(knn, X_test, y_test, cv=10, n_jobs=1, scoring = 'accuracy')

#Độ chính xác trung bình
print('Average Accucy: \t{0:.4f}\n'.format((res.mean())))

print('Standard Deviation: \t{0:.4f}\n'.format((res.std())))

print('Confusion Matrix :\n{}\n'.format(confusion_matrix(y_test, knn.predict(X_test))))

print('Accuracy Score :\t\t{}%'.format(round(knn.score( X_test, y_test)*100,2)))

print ('Train Accuracy - : {}%'.format(round(knn.score( X_train, y_train)*100,2)))
print ('Test Accuracy - : {}%'.format(round(knn.score( X_test, y_test)*100,2)))

plot_confusion_matrix(knn, X_test, y_test)
# fig.savefig('matrix_knn.png')

n_neighbors = np.arange(1, 20)
train_accuracy = np.empty(len(n_neighbors))
test_accuracy = np.empty(len(n_neighbors))
# Loop over different values of k
for i, k in enumerate(n_neighbors):
# Setup a k-NN Classifier with k neighbors: knn
 knn = KNeighborsClassifier(k)
# Fit the classifier to the training data
 knn.fit(X_train, y_train)
 train_accuracy[i] = knn.score(X_train,y_train)
 test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(n_neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(n_neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()

f1_score=accuracy_score
dt_f1 =f1_score(y_test, dt_pred)
knn_f1 = f1_score(y_test, kn_pred)

RF_f1 = f1_score(y_test, rf_pred)

x=['Decision Tree','KNN','Random Forest']
y=[dt_f1,knn_f1,RF_f1]

plt.figure(figsize=(20,20))
fig, ax = plt.subplots()
ax.bar(x, y, width=0.8)
plt.title('F1 Score Of Our Model')
plt.xlabel('Model')
plt.ylabel('F1 Score')
plt.show()
# fig.savefig('dt_rf_knn.png')

"""#ROC Curves"""

# Compute predicted probabilities: y_pred_prob
y_pred_prob_dt = dt.predict_proba(X_test)[:,1]
y_pred_prob_knn = knn.predict_proba(X_test)[:,1]
y_pred_prob_rf = rf.predict_proba(X_test)[:,1]

pred_prob = [y_pred_prob_dt,y_pred_prob_knn,y_pred_prob_rf]

# Generate ROC curve values: fpr, tpr, thresholds

fpr_1, tpr_1, thresholds_1 = roc_curve(y_test, y_pred_prob_dt)
fpr_2, tpr_2, thresholds_2 = roc_curve(y_test, y_pred_prob_knn)
fpr_3, tpr_3, thresholds_3 = roc_curve(y_test, y_pred_prob_rf)

# Plot ROC curve
plt.figure(figsize=(16,16))
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr_1, tpr_1, label = 'Tree decision')
plt.plot(fpr_2, tpr_2, label = 'KNN')
plt.plot(fpr_3, tpr_3, label = 'Random forest')

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(prop={'size':18}, loc='lower right')

plt.show()