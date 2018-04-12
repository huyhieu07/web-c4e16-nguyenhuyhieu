from gmail import GMail, Message
from models.reference import Order


gmail = GMail('vihoabinhnhanloai@gmail.com','thisishuyhieu')

contentz = '''
<p>Đơn h&agrave;ng của bạn đ&atilde; được vận chuyển, cảm ơn bạn đ&atilde; tin d&ugrave;ng dịch vụ của ch&uacute;ng t&ocirc;i!!!</p>
<p></p>
<p>--Muadongkhonglanh--&nbsp;</p>'''
msg = Message('Muadongkhonglanh',to = 'huyieu070109@gmail.com', html = contentz)

if is_accepted == '0':
    gmail.send(msg)
