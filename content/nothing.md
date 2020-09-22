<style>
.alert {
  padding: 20px;
  background-color: #f44336;
  color: white;
}

.closebtn {
  margin-left: 15px;
  color: white;
  font-weight: bold;
  float: right;
  font-size: 22px;
  line-height: 20px;
  cursor: pointer;
  transition: 0.3s;
}

.closebtn:hover {
  color: black;
}
</style>
<div class="alert">
  <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span> 
  <strong>Worning!</strong> Please update your text here.
</div>


<!--[TOC]在这里不可以用-->

<ul id="myTab" class="nav nav-tabs">
  <!-- active 指的是默认页 -->
  <li class="active">
    <!-- herf中名字于下文id对应 -->
    <!-- 这里只改herf和tab1 -->
    <a href="#tab1" data-toggle="tab">tab1</a>
  </li>
  <li><a href="#tab2" data-toggle="tab">tab2</a></li>
</ul>
<div id="myTabContent" class="tab-content" markdown="1">
  <!-- 此处的id与上文herf对应 其他的不要改-->
  <div class="tab-pane fade in active" id="tab1" markdown="1">
## Tab1
**这里输入markdown**
  </div>
  <div class="tab-pane fade" id="tab2" markdown="1">
# Tab2
**这里输入markdown**
  </div>
</div>