<script>
	import '../app.postcss';
    import { DarkMode } from 'flowbite-svelte';
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte'
</script>

<div>
    <Navbar let:hidden let:toggle rounded color="form">
        <NavBrand href="/">
            <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Demo</span>
        </NavBrand>
        <NavHamburger on:click={toggle} />
        <NavUl {hidden}>

        </NavUl>
        <DarkMode />
    </Navbar>
    <div class="mt-4 flex justify-center">
        <slot />
    </div>
</div>
