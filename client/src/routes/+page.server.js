export const actions = {
    default: async ({ request }) => {
        const data = await request.formData();

        try {
            const response = await fetch('http://127.0.0.1:5000/messages', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: data.get('name'),
                    message: data.get('message'),
                })
            })

            return await response.json()
        } catch (error) {
            console.log(error)
        }
    }
};
