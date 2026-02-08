-- SQL Portfolio: Reddit Database Validation
-- 1. Yoxlama: İstifadəçinin post sayının düzgün artmasını yoxlamaq
SELECT u.username, COUNT(p.post_id) as actual_posts, u.profile_post_count
FROM users u
JOIN posts p ON u.user_id = p.author_id
GROUP BY u.username, u.profile_post_count
HAVING COUNT(p.post_id) <> u.profile_post_count;

-- 2. Yoxlama: Ən çox səs alan 5 postu və onların kateqoriyalarını tapmaq
SELECT p.title, s.subreddit_name, p.upvotes
FROM posts p
INNER JOIN subreddits s ON p.subreddit_id = s.id
ORDER BY p.upvotes DESC
LIMIT 5;
