from http import HTTPStatus
import dashscope


def call_with_messages():
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': 'Please introduce Tongyi Qianwen and the main indicators of the current model, such as Context length, model, etc.?'}]

    response = dashscope.Generation.call(
        dashscope.Generation.Models.qwen_max,
        messages=messages,
        result_format='message',  # 将返回结果格式设置为 message
    )
    if response.status_code == HTTPStatus.OK:
        print(response)
    else:
        print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
            response.request_id, response.status_code,
            response.code, response.message
        ))


if __name__ == '__main__':
    call_with_messages()
