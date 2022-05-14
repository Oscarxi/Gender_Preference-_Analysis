import pandas as pd
import matplotlib.pyplot as plt

# Input
raw_data = pd.read_csv('Gender Preference Analysis/Transformed Data Set - Sheet1.csv')


# Color and Gender
# print(set(raw_data['Favorite Color']))
# 喜歡冷色系人數
cool_num_F = len(raw_data[(raw_data['Favorite Color'] == "Cool") & (raw_data['Gender'] == "F")])
cool_num_M = len(raw_data[(raw_data['Favorite Color'] == "Cool") & (raw_data['Gender'] == "M")])

# 無偏好色系人數
neutral_num_F = len(raw_data[(raw_data['Favorite Color'] == "Neutral") & (raw_data['Gender'] == "F")])
neutral_num_M = len(raw_data[(raw_data['Favorite Color'] == "Neutral") & (raw_data['Gender'] == "M")])

# 喜歡暖色系人數
warm_num_F = len(raw_data[(raw_data['Favorite Color'] == "Warm") & (raw_data['Gender'] == "F")])
warm_num_M = len(raw_data[(raw_data['Favorite Color'] == "Warm") & (raw_data['Gender'] == "M")])

# 建立新資料表
color_numbers = ['女性人數','男性人數']
color_index = ['Cool', 'Neutral', 'Warm']
datas = [cool_num_F,cool_num_M,
        neutral_num_F,neutral_num_M,
        warm_num_F,warm_num_M]

# 建立圖表
labels = ['cool_num_F', 'cool_num_M',
        'neutral_num_F', 'neutral_num_M',
        'warm_num_F', 'warm_num_M']
# 圖表設定
fig1, ax1 = plt.subplots()
ax1.pie(datas, labels = labels, autopct = '%.1f%%', shadow = False, startangle = 90, textprops = {'fontsize': 20})
ax1.set_title("Color Preference", size = 20)
ax1.legend(loc = "upper left")
fig1.set_size_inches(14,12)

# 輸出圖表
plt.show()


# Music Genre and Gender
# print(set(raw_data['Favorite Music Genre']))
Electronic_nums = len(raw_data[raw_data['Favorite Music Genre'] == "Electronic"])
Folk_Traditional_nums = len(raw_data[raw_data['Favorite Music Genre'] == "Folk/Traditional"])
Hip_hop_nums = len(raw_data[raw_data['Favorite Music Genre'] == "Hip hop"])
Jazz_Blues_nums = len(raw_data[raw_data['Favorite Music Genre'] == "Jazz/Blues"])
Pop_nums = len(raw_data[raw_data['Favorite Music Genre'] == "Pop"])
RnB_soul_nums = len(raw_data[raw_data['Favorite Music Genre'] == "R&B and soul"])
Rock_nums = len(raw_data[raw_data['Favorite Music Genre'] == "Rock"])

# 建立圖表
labels = ['Electronic', 'Folk/Traditional', 'Hip hop', 'Jazz/Blues', 'Pop', 'R&B and soul', 'Rock']
datas_music = [Electronic_nums, Folk_Traditional_nums, Hip_hop_nums, Jazz_Blues_nums, Pop_nums, RnB_soul_nums, Rock_nums]

# 圖表設定
fig1, ax1 = plt.subplots()
ax1.pie(datas_music, labels = labels, autopct = '%.1f%%', shadow = False, startangle = 90, textprops = {'fontsize': 20})
ax1.set_title("Music Genre Preference", size = 20)
ax1.legend(loc = "lower right")
fig1.set_size_inches(14,12)

# Output
plt.show()


# Beverage and Gender
# print(set(raw_data['Favorite Beverage']))
# 新增欄位:女性為1，男性為0
raw_data['F_counts'] = [ 0 if i == 'M' else 1 for i in raw_data['Gender']]
# 男性為1，女性為0
raw_data['M_counts'] = [ 0 if i == 'F' else 1 for i in raw_data['Gender']]

# 計算男女愛好酒精類別之人數
beverage_data = raw_data[['Favorite Beverage', 'F_counts', 'M_counts']]
beverage_comparison = beverage_data.groupby('Favorite Beverage').sum()

# 新增男女比例欄位
beverage_comparison['F_ratio'] = beverage_comparison['F_counts'] / (beverage_comparison['F_counts'] + beverage_comparison['M_counts'])
beverage_comparison['M_ratio'] = beverage_comparison['M_counts'] / (beverage_comparison['F_counts'] + beverage_comparison['M_counts'])
# print(beverage_comparison)


# Soft Drink and Color
# print(set(raw_data['Favorite Soft Drink']))
# 新增欄位:計算資料
raw_data['people_counts'] = 1

# 建立新資料表
soft_data = raw_data[['Favorite Color', 'Favorite Soft Drink', 'people_counts']]

# 觀察Soft Drink和Color的關係
soft_data.groupby(['Favorite Color', 'Favorite Soft Drink']).sum().reset_index()

# 製作圖表
datas_color_cool = [7, 18, 6, 6]
label_cool = ['coo1_7UP', 'cool_coca', 'cool_Fanta', 'cool_other']
fig1, ax2 = plt.subplots()
ax2.pie(datas_color_cool, labels = label_cool, autopct = '%.1f%%', shadow = False, startangle = 90, textprops = {'fontsize': 20})
ax2.set_title("Cool - Soft Drink", size = 20)
ax2.legend(loc = "lower right")
fig1.set_size_inches(16,8)

# Output
plt.show()

# 製作圖表
datas_color_Neutral = [2, 4, 1]
label_Neutral = ['Neutral_7UP', 'Neutral_coca', 'Neutral_Fanta']
fig1, ax3 = plt.subplots()
ax3.pie(datas_color_Neutral, labels = label_Neutral, autopct = '%.1f%%', shadow = False, startangle = 90, textprops = {'fontsize': 20})
ax3.set_title("Neutral - Soft Drink", size = 20)
ax3.legend(loc = "lower left")
fig1.set_size_inches(10,8)

# Output
plt.show()

# 製作圖表
datas_color_Warm = [4, 10, 7, 1]
label_Warm = ['Warm_7UP', 'Warm_coca', 'Warm_Fanta', 'Warm_other']
fig1, ax1 = plt.subplots()
ax1.pie(datas_color_Warm, labels = label_Warm, autopct = '%.1f%%', shadow = False, startangle = 90, textprops = {'fontsize': 20})
ax1.set_title("Warm - Soft Drink", size = 20)
ax1.legend(loc = "lower right")
fig1.set_size_inches(14,16)

# Output
plt.show()