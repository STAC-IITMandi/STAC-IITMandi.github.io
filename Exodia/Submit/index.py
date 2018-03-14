import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'Entries/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'svg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return """
    <!DOCTYPE html>

<html lang="eng_US">
<!-- To declare your language - read more here: https://www.w3.org/International/questions/qa-html-language-declarations -->
<head>
<title>Submit Entries</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<link href="layout/styles/layout.css" rel="stylesheet" type="text/css" media="all">
<link href="../layout/styles/custom.css" rel="stylesheet" type="text/css" media="all">
</head>
<body id="top">
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- Top Background Image Wrapper -->
<div class="topspacer bgded overlay" style="background-image:url('../../images/demo/backgrounds/01.jpg');">
  <!-- ################################################################################################ -->
  <div class="wrapper row1">
    <header id="header" class="hoc clear">
      <!-- ################################################################################################ -->
      <div id="logo" align="center">
        <!-- <h1><a href="index.html">STAC-IITMandi</a></h1> -->
        <img align = "center" src="../../images/demo/stac.png" alt="STAC-IITMandi" style="width:20%;padding:0px;margin-bottom: 0px; ">
      </div>
      <!-- ################################################################################################ -->
      <nav id="mainav" class="fl_right">
        <ul class="clear">

            <li class="active"><a href="../index.html">Home</a></li>

          <li class="active"><a class="drop" href="#">Details</a>
            <ul>
              <!--<li><a href="pages/full-width.html">Full Width</a></li>-->
              <!--<li><a href="pages/sidebar-left.html">Sidebar Left</a></li>-->
              <li><a class="drop" href="../../pages/vision.html">Vision</a></li>
              <li><a class="drop" href="../../pages/vision.html">Inventory</a></li>
              <li><a class="drop" href="../../pages/vision.html">Co-ordinators</a>
                <ul>
                  <li><a href="http://students.iitmandi.ac.in/~b16145/">Shreyas Bapat</a></li>
                  <li><a href="#">Garvit Mathur</a></li>
                </ul>
              </li>
              <li><a class="drop" href="../Exodia">Exodia</a></li>
              <li><a class="drop" href="../../pages/vision.html">Advisors</a></li>
              <li><a class="drop" href="../../pages/vision.html">Telescopes@STAC</a>
                <ul>
                  <li><a href="../../pages/vision.html">150mm SPACE EQ.</a></li>
                  <li><a href="../../pages/vision.html">Celestron 130EQ</a></li>
                  <li><a href="../../pages/vision.html">90mm Dobsonian</a></li>
                  <li><a href="../../pages/vision.html">12in Dobsonian</a></li>
                </ul>
              </li>
              <li><a class="drop" href="../../pages/vision.html">How it Began</a></li>
              <li><a class="drop" href="../../pages/vision.html">Notable Alumni</a></li>
              <!--<li><a href="pages/sidebar-right.html">Sidebar Right</a></li>-->
              <!--<li><a href="pages/basic-grid.html">Basic Grid</a></li>-->
            </ul>
          </li>
          <li><a href="../../Gallery">Gallery</a></li>
          <li><a href="../">Exodia</a></li>

        </ul>
      </nav>
    </header>
    <!-- ################################################################################################ -->
  </div>
  <!-- ################################################################################################ -->
  <!-- ################################################################################################ -->
  <!-- ################################################################################################ -->
  <div id="breadcrumb" class="hoc clear">
    <!-- ################################################################################################ -->
    <h1 class="heading" align="center"><strong>EXODIA '18 - Submissions</strong></h1>
    <h1 class="heading" align="center"><strong>Zenith Horizon</strong></h1>

    <!-- ################################################################################################ -->
  </div>
  <!-- ################################################################################################ -->
</div>
<!-- End Top Background Image Wrapper -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<div class="wrapper row3">
  <main class="hoc container clear"> 
    <!-- main body -->
    <!-- ################################################################################################ -->
    <div class="content"> 
 <h2>Make Submissions! Hail Exodia! </h2>
        <form action="#" method="post" enctype="multipart/form-data">
          <div class="one_third first">
            <label for="name">Name <span>*</span></label>
            <input type="text" name="name" id="name" value="" size="22" required>
          </div>
          <div class="one_third">
            <label for="email">Mail <span>*</span></label>
            <input type="email" name="email" id="email" value="" size="22" required>
          </div>
          <div class="one_third">
            <label for="url">Subject</label>
            <input type="url" name="url" id="url" value="" size="22">
          </div>
          <div class="one_third first">
            <label for="url">Location</label>
            <input type="url" name="url" id="url" value="" size="22">
          </div>
          <div class="block clear">
            <label for="comment">Brief Description of Photo (Optional)</label>
            <textarea name="comment" id="comment" cols="25" rows="10"></textarea>
          </div>
          <div>
            <input type="file">
            <input type="submit" name="submit" value="Submit Form">
            &nbsp;
            <input type="reset" name="reset" value="Reset Form">
          </div>
        </form>
      <!-- ################################################################################################ -->
      <!-- ################################################################################################ -->
      <!-- <nav class="pagination"> 
        <ul>
          <li><a href="#">&laquo; Previous</a></li>
          <li><a href="#">1</a></li> -->
          <!-- <li><a href="#">2</a></li>
          <li><strong>&hellip;</strong></li>
          <li><a href="#">6</a></li>
          <li class="current"><strong>7</strong></li>
          <li><a href="#">8</a></li>
          <li><a href="#">9</a></li>
          <li><strong>&hellip;</strong></li>
          <li><a href="#">14</a></li>
          <li><a href="#">15</a></li> -->
          <!-- <li><a href="#">Next &raquo;</a></li>
        </ul>
      </nav> -->
      <!-- ################################################################################################ -->
    </div>
    <!-- ################################################################################################ -->
    <!-- / main body -->
    <div class="clear"></div>
  </main>
</div>
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<div class="wrapper row4 bgded overlay" style="background-image:url('../images/demo/backgrounds/main3.jpg');">
  <footer id="footer" class="hoc clear">
    <!-- ################################################################################################ -->
    <div class="one_quarter first">
      <h6 class="heading">About Us</h6>
      <p class="btmspace-30">STAC is the hobby club under SnTC which deals in Astronomy, Astrophysics, Astrophotography, Space Technology etc.</p>
      <nav class="btmspace-30">
        <ul class="nospace">
          <li><a href="../index.html"><i class="fa fa-lg fa-home"></i></a></li>
          <li><a href="../pages/vision.html">About</a></li>
          <li><a href="../pages/vision.html">Contact</a></li>
        </ul>
      </nav>
      <ul class="faico clear">
       <!--  <li><a class="faicon-facebook" href="#"><i class="fa fa-facebook"></i></a></li>
        <li><a class="faicon-twitter" href="#"><i class="fa fa-twitter"></i></a></li>
        <li><a class="faicon-dribble" href="#"><i class="fa fa-dribbble"></i></a></li>
        <li><a class="faicon-linkedin" href="#"><i class="fa fa-linkedin"></i></a></li> -->
         <li><a class="faicon-facebook" href="http://facebook.com/stacIITMandi/"><i class="fa fa-facebook"></i></a></li>
      </ul>
    </div>
    <div class="one_quarter">
      <h6 class="heading">Reach out</h6>
      <ul class="nospace linklist contact">
        <li><i class="fa fa-map-marker"></i>
          <address>
          G1-101 , South Campus, IIT Mandi, Mandi(H.P.)- 175005
          </address>
        </li>
        <li><i class="fa fa-phone"></i> +91 (973) 621 0570</li>
        <li><i class="fa fa-fax"></i> +91 (811) 441 5628</li>
        <li><i class="fa fa-envelope-o"></i> stac@students.iitmandi.ac.in</li>
      </ul>
    </div>
    <div class="one_quarter">
      <h6 class="heading">Important Links</h6>
      <ul class="nospace linklist">
        <li><a target = "_blank" href="http://interiit.tech/#eventspagecontainer">Exoplanet Detection- Inter IIT Tech Meet</a></li>
        <li><a target = "_blank" href="http://interiit.tech/#eventspagecontainer">Orbital Simulator - Inter IIT Tech Meet</a></li>
        <li><a target = "_blank" href="../doc1.pdf">Proposal for Observatory</a></li>
        <li><a target = "_blank" href="http://exodia.in">Exodia Events</a></li>
        <li><a target = "_blank" href="http://exodia.in">Co-ordinators for events in Exodia</a></li>
      </ul>
    </div>
    <div class="one_quarter">
      <h6 class="heading">Important Notice</h6>
      <p class="btmspace-30">All the Activities of STAC are open for each and every person living in the campusof IIT Mandi. We declare ourselves an open club and we strongly believe that each and every person in the campus is a member of STAC. </p>
      <!--<form method="post" action="#">
        <fieldset>
          <legend>Newsletter:</legend>
          <input class="btmspace-15" type="text" value="" placeholder="Name">
          <input class="btmspace-15" type="text" value="" placeholder="Email">
          <button type="submit" value="submit">Submit</button>
        </fieldset>
      </form>-->
    </div>
    <!-- ################################################################################################ -->
  </footer>
</div>
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<div class="wrapper row5">
  <div id="copyright" class="hoc clear">
    <!-- ################################################################################################ -->
    <p class="fl_left">Copyright &copy; 2018 - All Rights Reserved - <a href="http://students.iitmandi.ac.in/~b16145/">Shreyas Bapat</a> & <a href="http://students.iitmandi.ac.in/~b17032/">Akash Dakoor</a></p>
    <!-- ################################################################################################ -->
  </div>
</div>
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<!-- ################################################################################################ -->
<a id="backtotop" href="#top"><i class="fa fa-chevron-up"></i></a>

<!-- JAVASCRIPTS -->
<script src="../layout/scripts/jquery.min.js"></script>
<script src="../layout/scripts/jquery.backtotop.js"></script>
<script src="../layout/scripts/jquery.mobilemenu.js"></script>
</body>
</html>
"""