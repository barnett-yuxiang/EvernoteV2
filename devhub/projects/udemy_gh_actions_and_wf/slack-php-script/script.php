<?php
require_once 'vendor/rmccue/requests/src/Autoload.php';
WpOrg\Requests\Autoload::register();

$response =  WpOrg\Requests\Requests::post(
  'YOUR SLACK WEBHOOK',
  array(
    'Content-Type' => 'application/json'
  ),
  json_encode(array (
    'blocks' => 
        array (
            array (
                "type" => "section",
                "text" => array (
                    "type" => "mrkdwn",
                    "text" => 'Message',
                ),
            ),
            array (
                "type" => "section",
                "fields" => array (
                    array (
                        "type" => "mrkdwn",
                        "text" => "*Repository:*\nRepository",
                    ),
                    array (
                        "type" => "mrkdwn",
                        "text" => "*Event:*\nEvent",
                    ),
                    array (
                        "type" => "mrkdwn",
                        "text" => "*Ref:*\nRef",
                    ),
                    array (
                        "type" => "mrkdwn",
                        "text" => "*SHA:*\nSHA",
                    ),
                ),
            ),
        ),
))
);

if(!$response->success) {
  echo $response->body;
  exit(1);
}