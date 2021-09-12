name_price = dict()
name_color = dict()

for name, price in name_price.items:
    if price < 1000:
        if name in name_color:
            for color in name_color[name]:
                if color !='red':
                    print('name: {}, color: {}'.format (name, color))
        else:
            print('name: {}, color: {}'.format (name, 'None'))

# 如果使用continue来写上面的代码会简洁些：用反向的思维来写代码
for name, price in name_price.items:
    if price >= 1000:
        continue
    if name not in name_color:
        print('name: {}, color: {}'.format (name, 'None'))
    for color in name_color[name]:
        if color == 'red':
            continue
        print('name: {}, color: {}'.format (name, color))