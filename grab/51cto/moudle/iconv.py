#!/usr/bin/python
#coding=utf-8

from ctypes import *
from ctypes.util import find_library
 
__all__ = ["iconv"]
 
def iconv(from_code, to_code, string):
    """
    from_code: 解码前字符串字符集
    to_code: 解码后字符串字符集
    string: 需要解码的数据
    """
 
    # 加载libc库
    _libc = CDLL(find_library("libc.6.so"))
 
    # 定义iconv_t指针类型
    _iconv_t = c_void_p
 
    # 声明iconv_open(3)原型
    _iconv_open = _libc.iconv_open
    _iconv_open.argtypes = [c_char_p, c_char_p]
    _iconv_open.restype = _iconv_t
 
    # 打开iconv句柄
    cp = _iconv_open(c_char_p(to_code), c_char_p(from_code))
 
    # 初始化输入/输出缓存
    inlen = len(string)
    inbuf = create_string_buffer(string, inlen)
    inbytesleft = c_size_t(len(inbuf))
    p_inbuf = pointer(inbuf)
 
    outlen = inlen * 4 + 4
    outbuf = create_string_buffer(outlen)
    outbytesleft = c_size_t(len(outbuf))
    p_outbuf = pointer(outbuf)
 
    # 声明iconv(3)原型
    _iconv = _libc.iconv
    _iconv.argtypes = [_iconv_t,
                       POINTER(POINTER(ARRAY(c_char, inlen))), POINTER(c_size_t),
                       POINTER(POINTER(ARRAY(c_char, outlen))), POINTER(c_size_t)]
    _iconv.restype = c_size_t
 
    # iconv编码转换
    _iconv(cp, byref(p_inbuf), byref(inbytesleft), byref(p_outbuf), byref(outbytesleft))
    result = outbuf.value[:outbytesleft.value]
 
    # 声明iconv_close(3)原型
    _iconv_close = _libc.iconv_close
    _iconv_close.argtypes = [_iconv_t]
    _iconv_close.restype = c_int
 
    # 关闭iconv句柄
    _iconv_close(cp)
 
    return result
 
if __name__ == "__main__":
 
    # 声明本地语言环境
    from locale import setlocale, LC_ALL
 
    setlocale(LC_ALL, 'en_US.UTF-8')
 
    t = u"你好，世界！"
    i = iconv("UTF-8", "GB18030", t.encode('UTF-8'))
    print u"TEST: IN: '%s'" % t
    print u"TEST: OUT: '%s'" % i.decode('GB18030')
