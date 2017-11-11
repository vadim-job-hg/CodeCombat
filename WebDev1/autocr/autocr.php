<?php
function scandir_by_mtime($folder) {
    var_dump($folder);
    $dircontent = scandir($folder);
    $arr = array();
    foreach($dircontent as $filename) {
        if ($filename != '.' && $filename != '..') {
            $arr[] = $filename;
        }
    }
    if (!ksort($arr)) return false;
    return $arr;
}

$files = scandir_by_mtime(dirname(__FILE__));
var_dump($files);
foreach ($files as $file){
    if($file!=='hero.png' && $file!=='Readme.md'){
        $fileName = explode('.', $file)[0];
        @mkdir($fileName);
        @rename($file, $fileName.DIRECTORY_SEPARATOR.$file);
        copy('hero.png', $fileName.DIRECTORY_SEPARATOR.'hero.png');
        @copy('Readme.md', $fileName.DIRECTORY_SEPARATOR.'Readme.md');

    }

}
?>