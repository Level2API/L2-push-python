# -*- coding: utf-8 -*-
# 此Demo只是演示接入过程

import grpc
import entity_pb2
import proxy_pb2_grpc
import threading
from multiprocessing import Process

# 代理服务器监听的地址和端口
ServerConnect = grpc.insecure_channel('localhost:5000')
Stub = proxy_pb2_grpc.ProxyStub(ServerConnect)


# 查询订阅
def get_subscription():
    # rep返回code为1代表成功,其余状态码可参考接入文档,data是返回订阅股票的情况
    Result = Stub.GetSubscription(entity_pb2.Void())
    print(Result)


# 新增订阅
def add_subscription():
    # 实例ProtoBuf协议的方法
    String = entity_pb2.String()
    # 修改协议的值
    # 2:市场代码标识(1为上海证券,2为深圳证券)
    # 000002:股票代码
    # 15:订阅全部标识(1为逐笔成交,2为逐笔委托,4为委托队列,8为股票十档行情,如果想全部订阅可直接填入15,原理是1+2+4+8,如果想订阅某几个行情将几个行情标识相加即可)
    String.value = '2_000002_15'
    # String.value = '2_000001_15,2_000002_5,2_000003_12,批量订阅'
    # rep返回code为1代表成功,其余状态码可参考接入文档
    Result = Stub.AddSubscription(String)
    print(Result)


# 取消订阅
def del_subscription():
    # 实例ProtoBuf协议的方法
    String = entity_pb2.String()
    # 修改协议的值
    # 2:市场代码标识(1为上海证券,2为深圳证券)
    # 000002:股票代码
    # 15:取消全部标识(1为逐笔成交,2为逐笔委托,4为委托队列,8为股票十档行情,如果想全部取消可直接填入15,原理是1+2+4+8,如果想取消某几个行情将几个行情标识相加即可)
    String.value = '2_000002_15'
    # String.value = '2_000001_15,2_000002_5,2_000003_12,批量取消'
    # rep返回code为1代表成功,其余状态码可参考接入文档
    Result = Stub.DelSubscription(String)
    print(Result)


# 推送逐笔成交行情数据
def tick_record_stream():
    StreamResult = Stub.NewTickRecordStream(entity_pb2.Void())
    # 用For循环就可以不断消费数据
    for Result in StreamResult:
        print(Result)


# 推送逐笔委托行情数据
def order_record_stream():
    StreamResult = Stub.NewOrderRecordStream(entity_pb2.Void())
    # 用For循环就可以不断消费数据
    for Result in StreamResult:
        print(Result)


# 推送委托队列行情数据
def order_queue_record_stream():
    StreamResult = Stub.NewOrderQueueRecordStream(entity_pb2.Void())
    # 用For循环就可以不断消费数据
    for Result in StreamResult:
        print(Result)


# 推送股票十档行情行情数据
def stock_quote_record_stream():
    StreamResult = Stub.NewStockQuoteRecordStream(entity_pb2.Void())
    # 用For循环就可以不断消费数据
    for Result in StreamResult:
        print(Result)


if __name__ == '__main__':
    # 可以使用多线程并发接收推送数据
    ThreadOne = threading.Thread(target=tick_record_stream)
    ThreadTwo = threading.Thread(target=order_record_stream)
    ThreadThree = threading.Thread(target=order_queue_record_stream)
    ThreadFour = threading.Thread(target=stock_quote_record_stream)
    # 多进程并发接收推送数据
    # ProcessOne = Process(target=tick_record_stream)
    # ProcessTwo = Process(target=order_record_stream)
    # ProcessThree = Process(target=order_queue_record_stream)
    # ProcessFour = Process(target=stock_quote_record_stream)

    # 这设置为随主线程退出子线程,避免产生孤儿或僵尸线程
    ThreadOne.daemon = True
    ThreadTwo.daemon = True
    ThreadThree.daemon = True
    ThreadFour.daemon = True
    # ProcessOne.daemon = True
    # ProcessTwo.daemon = True
    # ProcessThree.daemon = True
    # ProcessFour.daemon = True

    # 有一点值得注意一下,假如订阅的股票相对活跃,推送的数据就不会有休眠的状态出现,因为Python的GIL锁,所以用多线程接收推送效率不显著,这个时候可以考虑用多进程来接收推送
    ThreadOne.start()
    ThreadTwo.start()
    ThreadThree.start()
    ThreadFour.start()
    # ProcessOne.start()
    # ProcessTwo.start()
    # ProcessThree.start()
    # ProcessFour.start()

    ThreadOne.join()
    ThreadTwo.join()
    ThreadThree.join()
    ThreadFour.join()
    # ProcessOne.join()
    # ProcessTwo.join()
    # ProcessThree.join()
    # ProcessFour.join()
