from fake_keepall import convert_html

TEST_HTML = '''
<html>
<body>
    <div>안녕하세요 안녕하세요</div>
    <p>안녕하세요 안녕하세요</p>
    <div>
        <p>안녕하세요 안녕하세요</p>
        <li>안녕하세요 안녕하세요</li>
    </div>
    <li>안녕하세요 안녕하세요</li>
    <p>
        <span>안녕하세요 안녕하세요</span>
    </p>
</body>
</html>
'''


def test_with_default_options():
    output = '''<html>
 <body>
  <div>
   <span style="white-space: nowrap;">
    안녕하세요
   </span>
   <span style="white-space: nowrap;">
    안녕하세요
   </span>
  </div>
  <p>
   <span style="white-space: nowrap;">
    안녕하세요
   </span>
   <span style="white-space: nowrap;">
    안녕하세요
   </span>
  </p>
  <div>
   <p>
    <span style="white-space: nowrap;">
     안녕하세요
    </span>
    <span style="white-space: nowrap;">
     안녕하세요
    </span>
   </p>
   <li>
    <span style="white-space: nowrap;">
     안녕하세요
    </span>
    <span style="white-space: nowrap;">
     안녕하세요
    </span>
   </li>
  </div>
  <li>
   <span style="white-space: nowrap;">
    안녕하세요
   </span>
   <span style="white-space: nowrap;">
    안녕하세요
   </span>
  </li>
  <p>
   <span>
    <span style="white-space: nowrap;">
     안녕하세요
    </span>
    <span style="white-space: nowrap;">
     안녕하세요
    </span>
   </span>
  </p>
 </body>
</html>
'''
    assert convert_html(TEST_HTML) == output


def test_with_p_tag():
    output = '''<html>
 <body>
  <div>
   안녕하세요 안녕하세요
  </div>
  <p>
   <span style="white-space: nowrap;">
    안녕하세요
   </span>
   <span style="white-space: nowrap;">
    안녕하세요
   </span>
  </p>
  <div>
   <p>
    <span style="white-space: nowrap;">
     안녕하세요
    </span>
    <span style="white-space: nowrap;">
     안녕하세요
    </span>
   </p>
   <li>
    안녕하세요 안녕하세요
   </li>
  </div>
  <li>
   안녕하세요 안녕하세요
  </li>
  <p>
   <span>
    안녕하세요 안녕하세요
   </span>
  </p>
 </body>
</html>
'''
    assert convert_html(TEST_HTML, ['p']) == output


def test_with_custom_class():
    output = '''<html>
 <body>
  <div>
   <span class="custom">
    안녕하세요
   </span>
   <span class="custom">
    안녕하세요
   </span>
  </div>
  <p>
   <span class="custom">
    안녕하세요
   </span>
   <span class="custom">
    안녕하세요
   </span>
  </p>
  <div>
   <p>
    <span class="custom">
     안녕하세요
    </span>
    <span class="custom">
     안녕하세요
    </span>
   </p>
   <li>
    <span class="custom">
     안녕하세요
    </span>
    <span class="custom">
     안녕하세요
    </span>
   </li>
  </div>
  <li>
   <span class="custom">
    안녕하세요
   </span>
   <span class="custom">
    안녕하세요
   </span>
  </li>
  <p>
   <span>
    <span class="custom">
     안녕하세요
    </span>
    <span class="custom">
     안녕하세요
    </span>
   </span>
  </p>
 </body>
</html>
'''
    assert convert_html(TEST_HTML, None, 'custom') == output


def test_with_mixed_sibling_tags():
    test_html = '<html><body><p>중간에 링크가 <a href="#">이렇게</a> 있네요</p></body></html>'  # noqa :E501
    output = '''<html>
 <body>
  <p>
   <span style="white-space: nowrap;">
    중간에
   </span>
   <span style="white-space: nowrap;">
    링크가
   </span>
   <a href="#">
    이렇게
   </a>
   <span style="white-space: nowrap;">
    있네요
   </span>
  </p>
 </body>
</html>'''
    assert convert_html(test_html) == output
