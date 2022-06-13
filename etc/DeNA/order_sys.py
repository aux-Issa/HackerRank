def main(lines):
  step = int(lines.pop(0))
  if step==1:
    num_menu_type = int(lines.pop(0))
    menu_info = [lines.pop(0).split(" ") for _ in range(num_menu_type)]
    menu_info = {int(i[0]):[int(i[1]),int(i[2])] for i in menu_info}
    order_info = [order.split(" ") for order in lines]
    for i in order_info:
      i.pop(0)
      i[:] = map(int, i)
    # print(order_info)
    # menu_info = {料理番号:[初期在庫数，価格]}
    # order_info = [[席番号, 料理番号，注文数]...]
    for order in order_info:
      if menu_info[order[1]][0] < order[2]:
        print('sold out ' + str(order[0]))
      else:
        menu_info[order[1]][0] -= order[2]
        for i in range(order[2]):
          print('received order ' + str(order[0])+' '+str(order[1]))
  elif step == 2:
    # menu_and_MW_num = [メニューの種類，電子レンジの数]
    menu_and_MW_num = lines.pop(0).split(" ")
    menu_and_MW_num = list(map(int, menu_and_MW_num))
    menu_num = menu_and_MW_num[0]
    MW_num = menu_and_MW_num[1]

    menu_info = [lines.pop(0).split(" ") for _ in range(menu_num)]
    # menu_info = {料理番号:[初期在庫数，価格]}
    menu_info = {int(i[0]):[int(i[1]),int(i[2])] for i in menu_info}
    # orderと調理完了の時系列 [['order', 10, 10], ['complete', 101], ['order', 11, 11], ['order', 12, 12], ['complete', 100], ['complete', 101]]
    # ['order', 席番号, 料理番号]
    # ['complete', 料理番号]'
    order_and_completion = []
    for line in lines:
      if 'complete' in line:
        comp_info = line.split(" ")
        comp_info[1] = int(comp_info[1])
        order_and_completion.append(comp_info)
      elif 'received order' in line:
        order_info = line.split(" ")
        order_info.pop(0)
        order_info[0] = 'order'
        order_info[1] = int(order_info[1])
        order_info[2] = int(order_info[2])
        order_and_completion.append(order_info)
    
    print(order_and_completion)
    # MW_num: 使用可能な電子レンジ数
    # 調理待ち
    wait_stack = []
    # 調理完了待ち
    wait_comp_stack = []
    for inf in order_and_completion:
      if inf[0] == 'order':
        if MW_num > 0:
          # 作り始める料理番号を出力
          wait_comp_stack.append(inf[2])
          MW_num -= 1
          print(inf[2])
        elif MW_num == 0:
          wait_stack.append(inf[2])
          print('wait')
      elif inf[0] == 'complete':
        if inf[1] in wait_comp_stack:
          # 調理されていないorderがある時
          if len(wait_stack) > 0:
            # 調理完了
            wait_comp_stack.remove(inf[1])
            next_cook = wait_stack.pop(0)
            # 次の調理開始
            wait_comp_stack.append(next_cook)
            print('ok '+ str(next_cook))
          # orderが全て調理済みの時
          else:
            # 調理完了
            wait_comp_stack.remove(inf[1])
            MW_num += 1
            print('ok')
        else:
          print('unexpected input')

  elif step == 3:
    num_menu_type = int(lines.pop(0))
    menu_info = [lines.pop(0).split(" ") for _ in range(num_menu_type)]
    # menu_info = {料理番号:[初期在庫数，価格]}
    menu_info = {int(i[0]):[int(i[1]),int(i[2])] for i in menu_info}
    order = []
    completion = []
    # 完了とオーダーの受け取り#時系列 [['order', 10, 10], ['complete', 101], ['order', 11, 11], ['order', 12, 12], ['complete', 100], ['complete', 101]]
    # ['order', 席番号, 料理番号]
    # ['complete', 料理番号]'
    for line in lines:
      if 'complete' in line:
        comp_info = line.split(" ")
        comp_info[1] = int(comp_info[1])
        completion.append(comp_info)
      elif 'received order' in line:
        order_info = line.split(" ")
        order_info.pop(0)
        order_info[0] = 'order'
        order_info[1] = int(order_info[1])
        order_info[2] = int(order_info[2])
        order.append(order_info)

    # print(order)
    # print(completion)
    for comp_info in completion:
      menu_code = comp_info[1]
      for i in range(len(order)):
        if menu_code in order[i]:
          seat_code = order[i][1]
          order.pop(i)
          print('ready ' + str(seat_code)+' ' + str(menu_code))
          break
        else:
          print('error')
    # print('ready '+席番号+料理番号)
  elif step == 4:
    num_menu_type = int(lines.pop(0))
    menu_info = [lines.pop(0).split(" ") for _ in range(num_menu_type)]
    # menu_info = {料理番号:[初期在庫数，価格]}
    menu_info = {int(i[0]):[int(i[1]),int(i[2])] for i in menu_info}
    # 全ての時系列情報
    order_ready_check = []
    for line in lines:
      if 'received order' in line:
        order_info = line.split(" ")
        order_info.pop(0)
        order_info[0] = 'order'
        # 席番号
        order_info[1] = int(order_info[1])
        # 料理番号
        order_info[2] = int(order_info[2])
        order_ready_check.append(order_info)
      elif 'ready' in line:
        ready_info = line.split(" ")
        ready_info[0] = 'ready'
        # 席番号
        ready_info[1] = int(ready_info[1])
        # 料理番号
        ready_info[2] = int(ready_info[2])
        order_ready_check.append(ready_info)
      elif 'check' in line:
        check_info = line.split(" ")
        # 席番号
        check_info[1] = int(check_info[1])
        order_ready_check.append(check_info)

    # print(order_ready_check)
    order_dic = {}
    sum_price_dic = {}
    # 種別,席番号，料理番号
    for info in order_ready_check:
      if info[0] == 'order':
        # 席番号
        if info[1] in order_dic:
          order_dic[info[1]].append(info[2])
          sum_price_dic[info[1]] += menu_info[info[2]][1]
        else:  
          order_dic[info[1]] = [info[2]]
          sum_price_dic[info[1]] = menu_info[info[2]][1]
      elif info[0] == 'ready':
        # readyすれば料理番号を除去
          order_dic[info[1]].remove(info[2])
      elif info[0] == 'check':
          if info[1] in order_dic and len(order_dic[info[1]]) == 0:
            print(sum_price_dic[info[1]])
            sum_price_dic[info[1]]=0
          elif not info[1] in order_dic:
          # 席にそもそもオーダーがない
            print(0)
          else:
            print('please wait')
          


# check 10 = 席番号
test_case1 = [
  '1',
  '2', 
  '100 5 700', 
  '50 2 300', 
  'order 13 100 4',
  'order 12 100 2',
  'order 11 100 1'
  ]
test_case2 = [
  '2',
  '2 2', 
  '100 5 700', 
  '101 5 300', 
  'received order 10 100',
  'complete 101',
  'received order 11 100',
  'received order 12 101',
  'complete 100',
  'complete 101'
  ]
test_case3 = [
  '3',
  '1', 
  '100 5 700', 
  'received order 10 100',
  'received order 11 100',
  'complete 100',
  'received order 10 100',
  'complete 100',
  'complete 100'
  ]
test_case4 = [
  '4',
  '1', 
  '100 5 700', 
  'received order 10 100',
  'ready 10 100',
  'check 10',
  'received order 10 100',
  'check 10',
  'ready 10 100',
  'check 10'
  ]
main(test_case1)