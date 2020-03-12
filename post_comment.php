<?php
require('Persistence.php');

$db = new Persistence();
if( $db->add_comment($_POST) ) {
  header( 'Location: index.php' );
}
else {
  header( 'Location: index.php?error=Your comment was not posted due to errors in your form submission' );
}
?>

<?php
require('Persistence.php');
$comment_post_ID = 1;
$db = new Persistence();
$comments = $db->get_comments($comment_post_ID);
$has_comments = (count($comments) > 0);
?>