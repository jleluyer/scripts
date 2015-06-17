


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>seq_crumbs/crumbs/sff_extract.py at master · JoseBlanca/seq_crumbs · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png">
    <meta name="hostname" content="github-fe116-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 2.0.0p247-github5 (2013-06-27) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="xhr-socket" href="/_sockets" />
    
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="84CB75057E93CD307523337D2" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="V7++HAyPjX/BWBZBRARreyD7CdIVp00qIkOQ22awUiI=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-a519fa01e3b08983e91c1cc20d53d362af289489.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-4227a5af2b2917601978281e240aa06e4fe1c1dc.css" media="all" rel="stylesheet" type="text/css" />
    

    

      <script src="https://github.global.ssl.fastly.net/assets/frameworks-f86a2975a82dceee28e5afe598d1ebbfd7109d79.js" type="text/javascript"></script>
      <script src="https://github.global.ssl.fastly.net/assets/github-ec93103a5c1fe6c06e925d30927bcb73be0ce174.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="ddf526ed0791d93e41c2d18cb9c068df">

        <link data-pjax-transient rel='permalink' href='/JoseBlanca/seq_crumbs/blob/230a73891ef64a8b9a6c51541f5158d0c237106a/crumbs/sff_extract.py'>
  <meta property="og:title" content="seq_crumbs"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/JoseBlanca/seq_crumbs"/>
  <meta property="og:image" content="https://github.global.ssl.fastly.net/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="seq_crumbs - Little sequence file utilities meant to work within Unix pipelines"/>

  <meta name="description" content="seq_crumbs - Little sequence file utilities meant to work within Unix pipelines" />

  <meta content="157491" name="octolytics-dimension-user_id" /><meta content="JoseBlanca" name="octolytics-dimension-user_login" /><meta content="4883197" name="octolytics-dimension-repository_id" /><meta content="JoseBlanca/seq_crumbs" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="4883197" name="octolytics-dimension-repository_network_root_id" /><meta content="JoseBlanca/seq_crumbs" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/JoseBlanca/seq_crumbs/commits/master.atom" rel="alternate" title="Recent Commits to seq_crumbs:master" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production  vis-public page-blob">
    <div class="wrapper">
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/signup">Sign up</a>
      <a class="button" href="/login?return_to=%2FJoseBlanca%2Fseq_crumbs%2Fblob%2Fmaster%2Fcrumbs%2Fsff_extract.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="JoseBlanca/seq_crumbs"
      data-branch="master"
      data-sha="59a7e129411c3be87a46c07cf6b25b058ab9c239"
  >

    <input type="hidden" name="nwo" value="JoseBlanca/seq_crumbs" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>


      


          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
  <a href="/login?return_to=%2FJoseBlanca%2Fseq_crumbs"
  class="minibutton with-count js-toggler-target star-button entice tooltipped upwards"
  title="You must be signed in to use this feature" rel="nofollow">
  <span class="octicon octicon-star"></span>Star
</a>
<a class="social-count js-social-count" href="/JoseBlanca/seq_crumbs/stargazers">
  13
</a>

  </li>

    <li>
      <a href="/login?return_to=%2FJoseBlanca%2Fseq_crumbs"
        class="minibutton with-count js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-git-branch"></span>Fork
      </a>
      <a href="/JoseBlanca/seq_crumbs/network" class="social-count">
        4
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/JoseBlanca" class="url fn" itemprop="url" rel="author"><span itemprop="title">JoseBlanca</span></a></span
          ><span class="repohead-name-divider">/</span><strong
          ><a href="/JoseBlanca/seq_crumbs" class="js-current-repository js-repo-home-link">seq_crumbs</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">

      <div class="repository-with-sidebar repo-container ">

        <div class="repository-sidebar">
            

<div class="repo-nav repo-nav-full js-repository-container-pjax js-octicon-loaders">
  <div class="repo-nav-contents">
    <ul class="repo-menu">
      <li class="tooltipped leftwards" title="Code">
        <a href="/JoseBlanca/seq_crumbs" aria-label="Code" class="js-selected-navigation-item selected" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /JoseBlanca/seq_crumbs">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped leftwards" title="Issues">
          <a href="/JoseBlanca/seq_crumbs/issues" aria-label="Issues" class="js-selected-navigation-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /JoseBlanca/seq_crumbs/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>2</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped leftwards" title="Pull Requests"><a href="/JoseBlanca/seq_crumbs/pulls" aria-label="Pull Requests" class="js-selected-navigation-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /JoseBlanca/seq_crumbs/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="repo-menu-separator"></div>
    <ul class="repo-menu">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/JoseBlanca/seq_crumbs/pulse" aria-label="Pulse" class="js-selected-navigation-item " data-pjax="true" data-selected-links="pulse /JoseBlanca/seq_crumbs/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/JoseBlanca/seq_crumbs/graphs" aria-label="Graphs" class="js-selected-navigation-item " data-pjax="true" data-selected-links="repo_graphs repo_contributors /JoseBlanca/seq_crumbs/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/JoseBlanca/seq_crumbs/network" aria-label="Network" class="js-selected-navigation-item js-disable-pjax" data-selected-links="repo_network /JoseBlanca/seq_crumbs/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

            <div class="only-with-full-nav">
              

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/JoseBlanca/seq_crumbs.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/JoseBlanca/seq_crumbs.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/JoseBlanca/seq_crumbs" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/JoseBlanca/seq_crumbs" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="octicon help tooltipped upwards" title="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>



                <a href="/JoseBlanca/seq_crumbs/archive/master.zip"
                   class="minibutton sidebar-button"
                   title="Download this repository as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
            </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:c614eecfe3c93da6f45ea12428e6d662 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:c614eecfe3c93da6f45ea12428e6d662 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/JoseBlanca/seq_crumbs/find/master" data-pjax data-hotkey="t" style="display:none">Show File Finder</a>

<div class="file-navigation">
  


<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/JoseBlanca/seq_crumbs/blob/master/crumbs/sff_extract.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" data-skip-pjax="true" rel="nofollow" title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/JoseBlanca/seq_crumbs/tree/v0.1.5/crumbs/sff_extract.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="v0.1.5" data-skip-pjax="true" rel="nofollow" title="v0.1.5">v0.1.5</a>
            </div> <!-- /.select-menu-item -->
            <div class="select-menu-item js-navigation-item ">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/JoseBlanca/seq_crumbs/tree/v0.1.3/crumbs/sff_extract.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="v0.1.3" data-skip-pjax="true" rel="nofollow" title="v0.1.3">v0.1.3</a>
            </div> <!-- /.select-menu-item -->
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/JoseBlanca/seq_crumbs" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">seq_crumbs</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/JoseBlanca/seq_crumbs/tree/master/crumbs" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">crumbs</span></a></span><span class="separator"> / </span><strong class="final-path">sff_extract.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="crumbs/sff_extract.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://2.gravatar.com/avatar/c89921ae4ffed4ba1f35d8523e23fd1d?d=https%3A%2F%2Fa248.e.akamai.net%2Fassets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png&amp;s=140" width="24" />
    <span class="author"><span rel="author">Peio</span></span>
    <time class="js-relative-date" datetime="2013-05-20T05:19:07-07:00" title="2013-05-20 05:19:07">May 20, 2013</time>
    <div class="commit-title">
        <a href="/JoseBlanca/seq_crumbs/commit/5aee7c3708cff4077efe05ef50a9ef627887f8f1" class="message" data-pjax="true" title="added write xml_traceinfo file option to sff_extract">added write xml_traceinfo file option to sff_extract</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li class="facebox-user-list-item">
          <img height="24" src="https://1.gravatar.com/avatar/e615f123fdb687de60a5a62adaad443e?d=https%3A%2F%2Fidenticons.github.com%2Ff21981d6c243cacbacff19ae3de35f1d.png&amp;s=140" width="24" />
          <a href="/JoseBlanca">JoseBlanca</a>
        </li>
      </ul>
    </div>
  </div>


<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>185 lines (160 sloc)</span>
        <span>7.003 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled js-entice" href=""
                 data-entice="You must be signed in to make or propose changes">Edit</a>
          <a href="/JoseBlanca/seq_crumbs/raw/master/crumbs/sff_extract.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/JoseBlanca/seq_crumbs/blame/master/crumbs/sff_extract.py" class="button minibutton ">Blame</a>
          <a href="/JoseBlanca/seq_crumbs/commits/master/crumbs/sff_extract.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
            <a class="minibutton danger empty-icon js-entice" href=""
               data-entice="You must be signed in and on a branch to make or propose changes">
            Delete
          </a>
      </div><!-- /.actions -->

    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>

            </td>
            <td class="blob-line-code">
                    <div class="highlight"><pre><div class='line' id='LC1'><span class="c"># Copyright 2012 Jose Blanca, Peio Ziarsolo, COMAV-Univ. Politecnica Valencia</span></div><div class='line' id='LC2'><span class="c"># This file is part of seq_crumbs.</span></div><div class='line' id='LC3'><span class="c"># seq_crumbs is free software: you can redistribute it and/or modify</span></div><div class='line' id='LC4'><span class="c"># it under the terms of the GNU General Public License as</span></div><div class='line' id='LC5'><span class="c"># published by the Free Software Foundation, either version 3 of the</span></div><div class='line' id='LC6'><span class="c"># License, or (at your option) any later version.</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><span class="c"># seq_crumbs is distributed in the hope that it will be useful,</span></div><div class='line' id='LC9'><span class="c"># but WITHOUT ANY WARRANTY; without even the implied warranty of</span></div><div class='line' id='LC10'><span class="c"># MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE.  See the</span></div><div class='line' id='LC11'><span class="c"># GNU General Public License for more details.</span></div><div class='line' id='LC12'><br/></div><div class='line' id='LC13'><span class="c"># You should have received a copy of the GNU General Public License</span></div><div class='line' id='LC14'><span class="c"># along with seq_crumbs. If not, see &lt;http://www.gnu.org/licenses/&gt;.</span></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><span class="kn">from</span> <span class="nn">__future__</span> <span class="kn">import</span> <span class="n">division</span></div><div class='line' id='LC17'><span class="kn">from</span> <span class="nn">array</span> <span class="kn">import</span> <span class="n">array</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'><span class="kn">from</span> <span class="nn">crumbs.utils.optional_modules</span> <span class="kn">import</span> <span class="n">SffIterator</span></div><div class='line' id='LC20'><br/></div><div class='line' id='LC21'><span class="c"># pylint: disable=R0913</span></div><div class='line' id='LC22'><br/></div><div class='line' id='LC23'><br/></div><div class='line' id='LC24'><span class="k">def</span> <span class="nf">_min_left_clipped_seqs</span><span class="p">(</span><span class="n">sff_fhand</span><span class="p">,</span> <span class="n">trim</span><span class="p">,</span> <span class="n">min_left_clip</span><span class="p">):</span></div><div class='line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;It generates sequences (as tuples) given a path to a SFF file.&#39;</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">SffIterator</span><span class="p">(</span><span class="n">sff_fhand</span><span class="p">,</span> <span class="n">trim</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC27'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">annots</span> <span class="o">=</span> <span class="n">record</span><span class="o">.</span><span class="n">annotations</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">clip_qual</span> <span class="o">=</span> <span class="n">annots</span><span class="p">[</span><span class="s">&#39;clip_qual_left&#39;</span><span class="p">]</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">clip_adapt</span> <span class="o">=</span> <span class="n">annots</span><span class="p">[</span><span class="s">&#39;clip_adapter_left&#39;</span><span class="p">]</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">clip</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">min_left_clip</span><span class="p">,</span> <span class="n">clip_qual</span><span class="p">,</span> <span class="n">clip_adapt</span><span class="p">)</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seq</span> <span class="o">=</span> <span class="n">record</span><span class="o">.</span><span class="n">seq</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">trim</span><span class="p">:</span></div><div class='line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">record</span><span class="o">.</span><span class="n">annotations</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">record</span> <span class="o">=</span> <span class="n">record</span><span class="p">[</span><span class="n">clip</span><span class="p">:]</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">annots</span><span class="p">[</span><span class="s">&#39;clip_qual_left&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">clip</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">annots</span><span class="p">[</span><span class="s">&#39;clip_adapter_left&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">clip</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seq</span> <span class="o">=</span> <span class="n">seq</span><span class="p">[:</span><span class="n">clip</span><span class="p">]</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span> <span class="o">+</span> <span class="n">seq</span><span class="p">[</span><span class="n">clip</span><span class="p">:]</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">quals</span> <span class="o">=</span> <span class="n">record</span><span class="o">.</span><span class="n">letter_annotations</span><span class="p">[</span><span class="s">&#39;phred_quality&#39;</span><span class="p">]</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">record</span><span class="o">.</span><span class="n">letter_annotations</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">record</span><span class="o">.</span><span class="n">seq</span> <span class="o">=</span> <span class="n">seq</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">dict</span><span class="o">.</span><span class="n">__setitem__</span><span class="p">(</span><span class="n">record</span><span class="o">.</span><span class="n">_per_letter_annotations</span><span class="p">,</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;phred_quality&quot;</span><span class="p">,</span> <span class="n">quals</span><span class="p">)</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">yield</span> <span class="n">record</span></div><div class='line' id='LC45'><br/></div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'><span class="k">class</span> <span class="nc">SffExtractor</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;This class extracts the reads from an SFF file&#39;</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">sff_fhands</span><span class="p">,</span> <span class="n">trim</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">min_left_clip</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">nucls_to_check</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span> <span class="n">max_nucl_freq_threshold</span><span class="o">=</span><span class="mf">0.5</span><span class="p">):</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;It inits the class&#39;</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fhands</span> <span class="o">=</span> <span class="n">sff_fhands</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">trim</span> <span class="o">=</span> <span class="n">trim</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">min_left_clip</span> <span class="o">=</span> <span class="n">min_left_clip</span></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># checking</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">nucls_to_check</span> <span class="o">=</span> <span class="n">nucls_to_check</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">max_nucl_freq_threshold</span> <span class="o">=</span> <span class="n">max_nucl_freq_threshold</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">nucl_counts</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC60'><br/></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nd">@property</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">seqs</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;It yields all sequences&#39;</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">fhand</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">fhands</span><span class="p">:</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_prepare_nucl_counts</span><span class="p">(</span><span class="n">fhand</span><span class="o">.</span><span class="n">name</span><span class="p">)</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">min_left_clip</span><span class="p">:</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seqs</span> <span class="o">=</span> <span class="n">SffIterator</span><span class="p">(</span><span class="n">fhand</span><span class="p">,</span> <span class="n">trim</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">trim</span><span class="p">)</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seqs</span> <span class="o">=</span> <span class="n">_min_left_clipped_seqs</span><span class="p">(</span><span class="n">fhand</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">trim</span><span class="p">,</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">min_left_clip</span><span class="p">)</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">record</span> <span class="ow">in</span> <span class="n">seqs</span><span class="p">:</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_update_nucl_counts</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">record</span><span class="o">.</span><span class="n">seq</span><span class="p">),</span> <span class="n">fhand</span><span class="o">.</span><span class="n">name</span><span class="p">)</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">yield</span> <span class="n">record</span></div><div class='line' id='LC74'><br/></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_prepare_nucl_counts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fpath</span><span class="p">):</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;It prepares the structure to store the nucleotide counts&#39;</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">counts</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;A&#39;</span><span class="p">:</span> <span class="n">array</span><span class="p">(</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">nucls_to_check</span><span class="p">),</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;T&#39;</span><span class="p">:</span> <span class="n">array</span><span class="p">(</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">nucls_to_check</span><span class="p">),</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;C&#39;</span><span class="p">:</span> <span class="n">array</span><span class="p">(</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">nucls_to_check</span><span class="p">),</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;G&#39;</span><span class="p">:</span> <span class="n">array</span><span class="p">(</span><span class="s">&#39;L&#39;</span><span class="p">,</span> <span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">nucls_to_check</span><span class="p">)}</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">nucl_counts</span><span class="p">[</span><span class="n">fpath</span><span class="p">]</span> <span class="o">=</span> <span class="n">counts</span></div><div class='line' id='LC82'><br/></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_update_nucl_counts</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">seq</span><span class="p">,</span> <span class="n">fpath</span><span class="p">):</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;Given a seq (as a string) it updates the nucleotide counts&#39;</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seq</span> <span class="o">=</span> <span class="n">seq</span><span class="p">[:</span><span class="bp">self</span><span class="o">.</span><span class="n">nucls_to_check</span><span class="p">]</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">counts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">nucl_counts</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">nucl</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">seq</span><span class="p">):</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">counts</span><span class="p">[</span><span class="n">fpath</span><span class="p">][</span><span class="n">nucl</span><span class="p">][</span><span class="n">index</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span>  <span class="c"># we do not count the lowercase letters</span></div><div class='line' id='LC92'><br/></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nd">@property</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">clip_advice</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;It checks how many positions have a high max nucl freq.&#39;</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">advices</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">fhand</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">fhands</span><span class="p">:</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fpath</span> <span class="o">=</span> <span class="n">fhand</span><span class="o">.</span><span class="n">name</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">counts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">nucl_counts</span><span class="p">[</span><span class="n">fpath</span><span class="p">]</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">treshold</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_nucl_freq_threshold</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pos_above_threshold</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seq_above_threshold</span> <span class="o">=</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">index</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">nucls_to_check</span><span class="p">):</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">num_nucls</span> <span class="o">=</span> <span class="p">[</span><span class="n">counts</span><span class="p">[</span><span class="s">&#39;A&#39;</span><span class="p">][</span><span class="n">index</span><span class="p">],</span> <span class="n">counts</span><span class="p">[</span><span class="s">&#39;T&#39;</span><span class="p">][</span><span class="n">index</span><span class="p">],</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">counts</span><span class="p">[</span><span class="s">&#39;C&#39;</span><span class="p">][</span><span class="n">index</span><span class="p">],</span> <span class="n">counts</span><span class="p">[</span><span class="s">&#39;G&#39;</span><span class="p">][</span><span class="n">index</span><span class="p">]]</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">tot_nucls</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">num_nucls</span><span class="p">)</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">tot_nucls</span><span class="p">:</span></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">continue</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">freq_nucls</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span> <span class="o">/</span> <span class="n">tot_nucls</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">num_nucls</span><span class="p">]</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">above_threshold</span> <span class="o">=</span> <span class="p">[</span><span class="n">i</span> <span class="o">&gt;=</span> <span class="n">treshold</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">freq_nucls</span><span class="p">]</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">any</span><span class="p">(</span><span class="n">above_threshold</span><span class="p">):</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">pos_above_threshold</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seq_above_threshold</span> <span class="o">+=</span> <span class="n">_get_nucl_with_max_freq</span><span class="p">(</span><span class="s">&#39;ATCG&#39;</span><span class="p">,</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">freq_nucls</span><span class="p">)</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">break</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">pos_above_threshold</span><span class="p">:</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">trim</span><span class="p">:</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># number of nucleotides to remove next time, the ones</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># that we have detected plus the ones already removed</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">advice</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">min_left_clip</span><span class="p">,</span> <span class="n">seq_above_threshold</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">advice</span> <span class="o">=</span> <span class="n">index</span><span class="p">,</span> <span class="n">seq_above_threshold</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">advice</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">advices</span><span class="p">[</span><span class="n">fpath</span><span class="p">]</span> <span class="o">=</span> <span class="n">advice</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">advices</span></div><div class='line' id='LC129'><br/></div><div class='line' id='LC130'><br/></div><div class='line' id='LC131'><span class="k">def</span> <span class="nf">_do_seq_xml</span><span class="p">(</span><span class="n">seq</span><span class="p">):</span></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">seq</span> <span class="o">=</span> <span class="n">seq</span><span class="o">.</span><span class="n">object</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">annots</span> <span class="o">=</span> <span class="n">seq</span><span class="o">.</span><span class="n">annotations</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">read_len</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">seq</span><span class="p">)</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">read_name</span> <span class="o">=</span> <span class="n">seq</span><span class="o">.</span><span class="n">id</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;E3MFGYR02FTGED&#39;</span> <span class="o">==</span> <span class="n">read_name</span><span class="p">:</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">annots</span><span class="p">,</span> <span class="n">read_len</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">qual_left</span> <span class="o">=</span> <span class="n">annots</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;clip_qual_left&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">qual_right</span> <span class="o">=</span> <span class="n">annots</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;clip_qual_right&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">vector_left</span> <span class="o">=</span> <span class="n">annots</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;clip_adapter_left&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">vector_right</span> <span class="o">=</span> <span class="n">annots</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;clip_adapter_right&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC142'><br/></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">vector_right</span> <span class="o">&gt;=</span> <span class="n">read_len</span><span class="p">:</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">vector_right</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">qual_right</span> <span class="o">&gt;=</span> <span class="n">read_len</span><span class="p">:</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">qual_right</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC147'><br/></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">qual_left</span> <span class="o">=</span> <span class="mi">0</span> <span class="k">if</span> <span class="n">qual_left</span> <span class="o">&lt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="n">qual_left</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">qual_right</span> <span class="o">=</span> <span class="mi">0</span> <span class="k">if</span> <span class="n">qual_right</span> <span class="o">&lt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="n">qual_right</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">vector_left</span> <span class="o">=</span> <span class="mi">0</span> <span class="k">if</span> <span class="n">vector_left</span> <span class="o">&lt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="n">vector_left</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">vector_right</span> <span class="o">=</span> <span class="mi">0</span> <span class="k">if</span> <span class="n">vector_right</span> <span class="o">&lt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="n">vector_right</span></div><div class='line' id='LC152'><br/></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">xml</span> <span class="o">=</span> <span class="s">&#39;</span><span class="se">\t</span><span class="s">&lt;trace&gt;</span><span class="se">\n</span><span class="s">&#39;</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">xml</span> <span class="o">+=</span> <span class="s">&#39;</span><span class="se">\t\t</span><span class="s">&lt;trace_name&gt;{}&lt;/trace_name&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">read_name</span><span class="p">)</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">qual_left</span><span class="p">:</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">xml</span> <span class="o">+=</span> <span class="s">&#39;</span><span class="se">\t\t</span><span class="s">&lt;clip_quality_left&gt;{}&lt;/clip_quality_left&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">qual_left</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">qual_right</span><span class="p">:</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">xml</span> <span class="o">+=</span> <span class="s">&#39;</span><span class="se">\t\t</span><span class="s">&lt;clip_quality_rigth&gt;{}&lt;/clip_quality_rigth&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">qual_right</span><span class="p">)</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">vector_left</span><span class="p">:</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">xml</span> <span class="o">+=</span> <span class="s">&#39;</span><span class="se">\t\t</span><span class="s">&lt;clip_vector_left&gt;{}&lt;/clip_vector_left&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">vector_left</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">vector_right</span><span class="p">:</span></div><div class='line' id='LC162'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">xml</span> <span class="o">+=</span> <span class="s">&#39;</span><span class="se">\t\t</span><span class="s">&lt;clip_vector_rigth&gt;{}&lt;/clip_vector_rigth&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">vector_right</span><span class="p">)</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">xml</span> <span class="o">+=</span> <span class="s">&#39;</span><span class="se">\t</span><span class="s">&lt;/trace&gt;</span><span class="se">\n</span><span class="s">&#39;</span></div><div class='line' id='LC164'><br/></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">xml</span></div><div class='line' id='LC166'><br/></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'><span class="k">def</span> <span class="nf">write_xml_traceinfo</span><span class="p">(</span><span class="n">seqs</span><span class="p">,</span> <span class="n">fhand</span><span class="p">):</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fhand</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;&lt;?xml version=&quot;1.0&quot;?&gt;</span><span class="se">\n</span><span class="s">&lt;trace_volume&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">seq</span> <span class="ow">in</span> <span class="n">seqs</span><span class="p">:</span></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fhand</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">_do_seq_xml</span><span class="p">(</span><span class="n">seq</span><span class="p">))</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">yield</span> <span class="n">seq</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fhand</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;&lt;/trace_volume&gt;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fhand</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span></div><div class='line' id='LC175'><br/></div><div class='line' id='LC176'><br/></div><div class='line' id='LC177'><span class="k">def</span> <span class="nf">_get_nucl_with_max_freq</span><span class="p">(</span><span class="n">nucls</span><span class="p">,</span> <span class="n">freq_nucls</span><span class="p">):</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;It returns the nucleotide with the maximum frequency&#39;</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">max_</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">freq</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">freq_nucls</span><span class="p">):</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">max_</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">or</span> <span class="n">max_</span> <span class="o">&lt;</span> <span class="n">freq</span><span class="p">:</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">max_</span> <span class="o">=</span> <span class="n">freq</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">nucl</span> <span class="o">=</span> <span class="n">nucls</span><span class="p">[</span><span class="n">index</span><span class="p">]</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">nucl</span></div></pre></div>
            </td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2013 <span title="0.03967s from github-fe116-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/JoseBlanca/seq_crumbs/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

    
  </body>
</html>

