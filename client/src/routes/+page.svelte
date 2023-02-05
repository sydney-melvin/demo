<script>
    import { Card, Activity, ActivityItem, Label, Input, Textarea, Button } from 'flowbite-svelte';

    const textAreaProps = {
        id: 'message',
        name: 'message',
        label: 'Your message',
        rows: 4,
        placeholder: 'Leave a comment...',
    };

    export let data
</script>

<div class="flex flex-col space-y-4">
    <Card class="max-h-96 overflow-y-scroll w-96">
        <div class="pl-1">
            {#if data.messages.length > 0}
                <Activity>
                    <ActivityItem activities={data.messages} />
                </Activity>
            {:else}
                <p>
                    No messages yet...
                </p>
            {/if}
        </div>
    </Card>
    <Card>
        <form class="flex flex-col space-y-3" method="POST">
            <div class="flex flex-col space-y-1">
                <Label>Name</Label>
                <Input id="name" name="name" placeholder="Enter your name" required />
            </div>
            <div class="flex flex-col space-y-1">
                <Label>Message</Label>
                <Textarea {...textAreaProps} />
            </div>
            <Button type="submit">Send</Button>
        </form>
    </Card>
</div>
