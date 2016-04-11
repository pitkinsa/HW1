<?php

$LOCAL_ROOT         = "/var/www/html;
$LOCAL_REPO_NAME    = "test";
$LOCAL_REPO         = "{$LOCAL_ROOT}/{$LOCAL_REPO_NAME}";
$REMOTE_REPO        = "https://github.com/CSE136Team7/HW1.git";
$DESIRED_BRANCH     = "master";

if (file_exists($LOCAL_REPO)) {
    shell_exec("rm -rf {$LOCAL_REPO}");
}

echo shell_exec("cd {$LOCAL_ROOT} && git clone {$REMOTE_REPO} {$LOCAL_REPO_NAME} && cd {$LOCAL_REPO} && git checkout {$DESIRED_BRANCH}");


die("done " . mktime());
?>
