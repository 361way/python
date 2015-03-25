#!/usr/bin/python
#coding=utf-8
import re
text = '''
<pre><code class="lang-c">#ifndef PHP_ARRAY_H
#define PHP_ARRAY_H
PHP_FUNCTION(uasort);
PHP_FUNCTION(uksort);
……
</code></pre>
<p>上面定义的排序函数：</p>
<pre><code class="lang-c">/* {{{ proto bool sort(array &amp;array_arg [, int sort_flags])
   Sort an array */
PHP_FUNCTION(sort)
{
    zval *array;
    long sort_type = PHP_SORT_REGULAR;

    if (zend_parse_parameters(ZEND_NUM_ARGS() TSRMLS_CC, "a|l", &amp;array, &amp;sort_type) == FAILURE) {
        RETURN_FALSE;
    }

    php_set_compare_func(sort_type TSRMLS_CC);

    if (zend_hash_sort(Z_ARRVAL_P(array), zend_qsort, php_array_data_compare, 1 TSRMLS_CC) == FAILURE) {
        RETURN_FALSE;
    }
    RETURN_TRUE;
}
/* }}} */
</code></pre>

<p>在代码中，看到了 </p>
'''

#print re.sub(r'(?ims)<pre><code\s+class="lang-\w+>"(.+?)</code>', r'\1', text)
r = re.compile(r'<pre><code.*?>(.+?)</code></pre>',re.S|re.I|re.M)
x = r.sub(r'<pre class="prettyprint linenums">\1</pre>', text)
print x


string = '''<a href="http://www.example.com/test.png"><img src="http://www.example.com/test.png" /></a>
Bla blabla
<a href="http://www.example.com/test.png"><img src="http://www.example.com/test.png" /></a>
bla bla bla'''

print re.sub(r'<a.*><img(.+)src="(.+?)(\/[^\/]+)"(.*/?)></a>', r'<div><img\1src="\2\3"\4></div>', string)
