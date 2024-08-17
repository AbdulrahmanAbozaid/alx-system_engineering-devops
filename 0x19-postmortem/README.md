# Postmortem: Apache 500 Internal Server Error on WordPress Site
![Resolution](./OutageResolve.webp)
## Issue Summary
Duration: 2024-08-16, 10:00 AM UTC - 11:15 AM UTC (1 hour 15 minutes)

Impact: The company's main WordPress website was down, resulting in a 500 Internal Server Error for all users. Approximately 100% of the users were affected, causing significant disruption to both internal and external stakeholders.

Root Cause: A typo in the WordPress wp-settings.php file, where .php was mistyped as .phpp, caused the Apache server to fail in processing the PHP file, leading to the 500 Internal Server Error.

## Timeline
10:00 AM: The issue was detected when monitoring systems flagged the website as down and unresponsive.
10:05 AM: An engineer confirmed the issue via a manual check using curl and observed the 500 Internal Server Error.
10:10 AM: The engineer began investigating the Apache logs, assuming the issue was related to server configuration.
10:25 AM: The logs did not provide clear insight, so strace was used to trace the Apache process to identify where the error occurred.
10:35 AM: The typo in the wp-settings.php file was identified as the root cause.
10:40 AM: The incident was escalated to the web development team to confirm the typo and begin resolution.
10:50 AM: A Puppet script was created to correct the typo by replacing .phpp with .php in the affected file.
11:00 AM: The Puppet script was executed, and the issue was resolved.
11:05 AM: The website was tested to confirm it was back online.
11:15 AM: Full functionality was restored, and all services were operating normally.
Root Cause and Resolution
Root Cause: The issue was caused by a typo in the wp-settings.php file, where .php was incorrectly typed as .phpp. This caused the Apache server to fail when attempting to process the file, resulting in a 500 Internal Server Error. This typo likely occurred during a manual file edit or deployment, where the change was not properly validated before going live.

## Resolution:
The issue was resolved by creating a Puppet script that automatically corrected the typo by replacing .phpp with .php in the affected file. The script was executed successfully, and the website was restored to full functionality.

## A Visual Representation (Because Diagrams Make Everything Better)
```scss
     _______
    |       |      (All is well)
    | .php  |      |
    |_______|
         |
         | (Oops, a wild typo!)
         V
     _______
    |       |      (All is chaos)
    | .phpp |      |
    |_______|
         |
         | (Enter Puppet script)
         V
     _______
    |       |      (All is well again)
    | .php  |      |
    |_______|
```

## Corrective and Preventative Measures
### Improvements:

Implement a code review process to catch typos and syntax errors before deploying changes to production.
Integrate automated testing to validate critical files like wp-settings.php during the deployment process.
Enhance monitoring and alerting systems to detect similar issues earlier.
Tasks:

- Patch the affected WordPress file to correct the typo.
- Add automated tests for PHP syntax validation during deployment.
- Set up monitoring on key WordPress files to detect unauthorized or incorrect changes.
- Conduct a review of the deployment process to prevent similar human errors in the future.
