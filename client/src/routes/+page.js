export async function load({ fetch }) {
    try {
        const response = await fetch('http://127.0.0.1:5000/messages')
        const json = await response.json()

        return {
            messages: json.messages.map(message => {
                message = JSON.parse(message)
                const date = new Date(message.created_at.replace(' ', 'T'))
                return {
                    title: message.user_name,
                    text: message.message,
                    date: date.toLocaleDateString() + ' @ ' + date.toLocaleTimeString(),
                }
            }),
        }
    } catch (error) {
        console.log(error)
    }
}