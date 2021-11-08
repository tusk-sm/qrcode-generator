from aiohttp import web
import io
import qrcode


async def create_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")    
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()
    return  imgByteArr


async def handle(request):

    if request.rel_url.query.get('data'):
        data = request.rel_url.query.get('data')

        if request.rel_url.query.get('charset'):

            charset = request.rel_url.query.get('charset')
            data = data.encode(charset) 
        
        imgByteArr = await create_code(data)
        response = web.StreamResponse(
            status=200,
            reason='OK',
            headers={'Content-Type': 'image/png'},
        )
        await response.prepare(request)
        await response.write(imgByteArr)
        await response.write_eof()
        return response

    else:

        text = '''Hello, world! This is qr-code generator.

It works like this:
https://qr-code-generator-t.herokuapp.com/?data=https://qr-code-generator-t.herokuapp.com/
Рut the string in the "data" query parameter.
If you need to encode a string, you can use the "charset" query parameter
        '''

        return web.Response(text=text)
