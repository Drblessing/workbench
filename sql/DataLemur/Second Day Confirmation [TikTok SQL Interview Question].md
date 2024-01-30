SELECT DISTINCT user_id
FROM emails e
JOIN texts t ON t.email_id = e.email_id
WHERE t.action_date = e.signup_date + INTERVAL '1 day'
AND t.signup_action = 'Confirmed'
