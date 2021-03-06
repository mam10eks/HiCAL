/* Mousetraps keyboard shortcuts */
Mousetrap.bind(['h', 's', 'r', 'u'], function(e, key) {
    var current_doc_id = $('#cal-document').data("doc-id");
    var doc_title = $('#document_title').text();
    var doc_snippet = $('#document_snippet').html();
    if(key == 'h') {
        send_judgment(current_doc_id, doc_title, doc_snippet, true, false, false, false, true);
    }
    else if(key == 's') {
        send_judgment(current_doc_id, doc_title, doc_snippet, false, true, false, false, true);
    }
    else if(key == 'r') {
        send_judgment(current_doc_id, doc_title, doc_snippet, false, false, true, false, true);
    }else if(key == 'u') {
        $('#reviewDocsModal').modal('toggle');
    }
    document.body.click();
    //if(queue.getLength() == 0){
    //    console.log("Getting the next patch of documents to judge");
    //    update_documents_to_judge_list();
    //}
});

Mousetrap.bind(['ctrl+f', 'command+f'], function(e) {
    e.preventDefault();
    post_ctrlf();
    $( "#search_content" ).focus();
    document.body.click();
    return false;
});

var search_content_form = document.getElementById('search_content');
var search_content_form_mousetrap = new Mousetrap(search_content_form);
search_content_form_mousetrap.bind(['ctrl+f', 'command+f'], function(e) {
    $( "#search_content" ).focus();
    post_ctrlf();
    document.body.click();
    return false;
});


function document_isEmpty(){
    var current_doc_id = $('#cal-document').data("doc-id");
    if(current_doc_id == '' || current_doc_id == 'None'){
        return true;
    }
    return false;
}


/* SEARCH BAR and highlighter */

$('#searchContentForm').submit(function (e) {
    e.preventDefault();
    $("#searchNext").click();
    return false;
});

var marked_matches_in_document_title = [];
var marked_matches_in_document_snippet = [];
var marked_matches_in_document_content = [];


$(function() {

  // the input field
  var $input = $("#search_content"),
    // clear button
    $clearBtn = $("button[data-search='clear']"),
    // prev button
    $prevBtn = $("button[data-search='prev']"),
    // next button
    $nextBtn = $("button[data-search='next']"),
    // the context where to search
    $content = $(".document-cal"),
    // list of selectors to ignore during the search
    $exclude = ["#show_full_doc_button", "#docno_text"],
    // jQuery object to save <mark> elements
    $results = "",
    // the class that will be appended to the current
    // focused element
    currentClass = "current",
    // top offset for the jump (the search bar)
    offsetTop = 50,
    // the current index of the focused element
    currentIndex = 0;

  /**
   * Jumps to the element matching the currentIndex
   */
  function jumpTo() {
    if ($results.length) {
      $input.addClass("greenBorder").css("border-color","#449D44");
      var position,
        $current = $results.eq(currentIndex);
      $results.removeClass(currentClass);
      if ($current.length) {
        $current.addClass(currentClass);
        position = $current.offset().top - offsetTop;
        window.scrollTo(0, position);
      }else{
        if(!$input.val()){
          $input.removeAttr('style');
        }else if ($input.is(':focus')){
          $input.addClass("redBorder").css("border-color","#C9302C");
        }
      }
    }
  }

  /**
   * Update dicts of matches in document title, snippet, and content
   */
  function updateMatchesDictionaries(){
    resetMatchesDict();
    var document_title_mark_instances = $("#document_title").find("mark");
    var document_snippet_mark_instances = $("#document_snippet").find("mark");
    var document_content_mark_instances = $("#document_content").find("mark");

    var i;
    for(i = 0; i < document_title_mark_instances.length; i++){
        var data = {
            "match": document_title_mark_instances[i].innerHTML,
            "wholeWord": get_surroundings_of_match(document_title_mark_instances[i])
        };
        marked_matches_in_document_title.push(data);
    }
    for(i = 0; i < document_snippet_mark_instances.length; i++){
        var data = {
            "match": document_snippet_mark_instances[i].innerHTML,
            "wholeWord": get_surroundings_of_match(document_snippet_mark_instances[i])
        };
        marked_matches_in_document_snippet.push(data);
    }
    for(i = 0; i < document_content_mark_instances.length; i++){
        var data = {
            "match": document_content_mark_instances[i].innerHTML,
            "wholeWord": get_surroundings_of_match(document_content_mark_instances[i])
        };
        marked_matches_in_document_content.push(data);
    }

  }

  /**
     * Gets the surrounding letters of a highlighted match.
     * E.g. "The company is ba<mark>se</mark>d in California"
     * retrun "based".
     */
    function get_surroundings_of_match(match){
        if(match.previousSibling != undefined && match.nextSibling != undefined){
            var prev = match.previousSibling.nodeValue;
            var next = match.nextSibling.nodeValue;
            if(prev == ""){
                prev = " ";
            }
            if(next == ""){
                next = " ";
            }
            var wholeMatch = [];
            var i;
            for(i = 0; i < prev.length; i++){
                var index = prev.length - i - 1;
                if(prev[index] != "" && prev[index] != " ") {
                    wholeMatch.push(prev[index]);
                } else {
                    break;
                }
            }
            wholeMatch.reverse();
            wholeMatch.push.apply(wholeMatch, match.innerHTML.split());
            for(i = 0; i < next.length; i++){
                if(next[i] != "" && next[i] != " "){
                    wholeMatch.push(next[i]);
                }else{
                    break;
                }
            }
            return wholeMatch.join("");
        }else {
            return null;
        }
    }

  function resetMatchesDict(){
    marked_matches_in_document_title = [];
    marked_matches_in_document_snippet = [];
    marked_matches_in_document_content = [];
  }

  /**
   * Searches for the entered keyword in the
   * specified context on input
   */
  $input.on("input", function() {
  	var searchVal = this.value;
    $content.unmark({
      done: function() {
        $content.mark(searchVal, {
          separateWordSearch: true,
          exclude: $exclude,
          done: function() {
            updateMatchesDictionaries();
            $results = $content.find("mark");
            currentIndex = 0;
            jumpTo();
          }
        });
      }
    });
  });

   $content.on( "updated", function() {
      var searchVal = $input.val();
       if(searchVal != undefined){
           $content.unmark({
              done: function () {
                  $content.mark(searchVal, {
                      separateWordSearch: true,
                      exclude: $exclude,
                      done: function () {
                          updateMatchesDictionaries();
                          $results = $content.find("mark");
                          currentIndex = 0;
                      }
                  });
              }
          });
       }

    });


  /**
   * Clears the search
   */
  $clearBtn.on("click", function() {
    resetMatchesDict();
    $content.unmark();
    $input.val("").focus();
  });

  /**
   * Next and previous search jump to
   */
  $nextBtn.add($prevBtn).on("click", function() {
    if ($results.length) {
      currentIndex += $(this).is($prevBtn) ? -1 : 1;
      if (currentIndex < 0) {
        currentIndex = $results.length - 1;
      }
      if (currentIndex > $results.length - 1) {
        currentIndex = 0;
      }
      jumpTo();
    }
  });
});
