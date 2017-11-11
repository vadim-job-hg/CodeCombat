<?php
function getDirContents($dir, &$results = array()){
    $files = scandir($dir);
    foreach($files as $key => $value){
        $path = realpath($dir.DIRECTORY_SEPARATOR.$value);
        if(is_dir($path) && $value != "." && $value != "..") {
            getDirContents($path, $results);
            $results[] = $path;
        }
    }
    return $results;
}

$dirs = getDirContents(dirname(__FILE__));
foreach($dirs as $dir){
    $fileName = $dir.DIRECTORY_SEPARATOR.end(explode(DIRECTORY_SEPARATOR, $dir)).".py";
    if(file_exists($fileName)){
        $url = false;
        $fileFirstLine = file($fileName)[0];
        echo $fileName.PHP_EOL;
        if(strpos($fileFirstLine, 'http://')!==false || strpos($fileFirstLine, 'https://')!==false){
            $url = str_replace(['#', ' ', "\n"], '', $fileFirstLine);
            echo $url.PHP_EOL;
        }
        $readme = file_get_contents($dir.DIRECTORY_SEPARATOR.'Readme.md');
        $readme = str_replace('{name}  - {name}', $fileName, $readme);
        if($url) $readme = str_replace('{link}', $url, $readme);
        $readme = str_replace('{link-file}', $dir, $readme);
        file_put_contents($dir.DIRECTORY_SEPARATOR.'Readme.md', $readme);
    }
}