SELECT
wp_posts.ID,
wp_posts.post_author,
wp_posts.post_date,
wp_posts.post_date_gmt,
wp_posts.post_content,
wp_posts.post_title,
wp_posts.post_excerpt,
wp_posts.post_status,
wp_posts.comment_status,
wp_posts.ping_status,
wp_posts.post_password,
wp_posts.post_name,
wp_posts.to_ping,
wp_posts.pinged,
wp_posts.post_modified,
wp_posts.post_modified_gmt,
wp_posts.post_content_filtered,
wp_posts.post_parent,
wp_posts.guid,
wp_posts.menu_order,
wp_posts.post_type,
wp_posts.post_mime_type,
wp_posts.comment_count
FROM
wp_posts
ORDER BY
wp_posts.ID DESC
LIMIT 10


SELECT
wp_postmeta.meta_id,
wp_postmeta.post_id,
wp_postmeta.meta_key,
wp_postmeta.meta_value
FROM
wp_postmeta
ORDER BY
wp_postmeta.meta_id DESC
LIMIT 20


SELECT
wp_term_relationships.object_id,
wp_term_relationships.term_taxonomy_id,
wp_term_relationships.term_order
FROM
wp_term_relationships
ORDER BY
wp_term_relationships.object_id DESC
LIMIT 20




8238	1	2014-11-13 15:50:40	2014-11-13 07:50:40		test		inherit	open	open		8237-revision			2014-11-13 15:50:40	2014-11-13 07:50:40		8237	http://www.geek521.com/?p=8238	0	revision		0

8237	1	2014-11-13 15:50:45	0000-00-00 00:00:00	this is test	test		draft	open	open					2014-11-13 15:50:45	2014-11-13 07:50:45		0	http://www.geek521.com/?p=8237	0	post		0



19201	8243	Delicacy_difficulty	1
19200	8243	_edit_last	1
19199	8243	_edit_lock	1416150776:1


8243	1	0