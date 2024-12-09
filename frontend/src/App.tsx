import React, { useState } from 'react'
import { Bell, MessageCircle, Users, FileText, Settings, LogOut } from 'lucide-react'
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

export default function App() {
    const [isLoggedIn, setIsLoggedIn] = useState(false)
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [activeTab, setActiveTab] = useState('news')

    const handleLogin = (e: React.FormEvent) => {
        e.preventDefault()
        // Simulate login process
        console.log('Login attempted with:', email, password)
        setIsLoggedIn(true)
    }

    const handleSSO = () => {
        // Simulate SSO login process
        console.log('SSO login attempted')
        setIsLoggedIn(true)
    }

    const handleLogout = () => {
        setIsLoggedIn(false)
        setEmail('')
        setPassword('')
    }

    if (!isLoggedIn) {
        return (
            <div className="flex items-center justify-center min-h-screen bg-gray-100">
                <Card className="w-[350px]">
                    <CardHeader>
                        <CardTitle>Welcome to CompanyNet</CardTitle>
                        <CardDescription>Sign in to access the employee communication platform</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <Tabs defaultValue="credentials" className="w-full">
                            <TabsList className="grid w-full grid-cols-2">
                                <TabsTrigger value="credentials">Credentials</TabsTrigger>
                                <TabsTrigger value="sso">SSO</TabsTrigger>
                            </TabsList>
                            <TabsContent value="credentials">
                                <form onSubmit={handleLogin} className="space-y-4">
                                    <div className="space-y-2">
                                        <Label htmlFor="email">Email</Label>
                                        <Input
                                            id="email"
                                            type="email"
                                            placeholder="name@company.com"
                                            value={email}
                                            onChange={(e) => setEmail(e.target.value)}
                                            required
                                        />
                                    </div>
                                    <div className="space-y-2">
                                        <Label htmlFor="password">Password</Label>
                                        <Input
                                            id="password"
                                            type="password"
                                            value={password}
                                            onChange={(e) => setPassword(e.target.value)}
                                            required
                                        />
                                    </div>
                                    <Button type="submit" className="w-full">Sign In</Button>
                                </form>
                            </TabsContent>
                            <TabsContent value="sso">
                                <div className="space-y-4">
                                    <p className="text-sm text-gray-500">Click below to sign in with your company SSO credentials.</p>
                                    <Button onClick={handleSSO} className="w-full">Sign In with SSO</Button>
                                </div>
                            </TabsContent>
                        </Tabs>
                    </CardContent>
                    <CardFooter>
                        <p className="text-sm text-gray-500">
                            Need help? Contact IT support at support@company.com
                        </p>
                    </CardFooter>
                </Card>
            </div>
        )
    }

    return (
        <div className="flex h-screen bg-gray-100">
            {/* Sidebar */}
            <div className="w-64 bg-white shadow-md">
                <div className="p-4">
                    <h1 className="text-2xl font-bold text-gray-800">CompanyNet</h1>
                </div>
                <nav className="mt-6">
                    <Button
                        variant={activeTab === 'news' ? 'default' : 'ghost'}
                        className="w-full justify-start"
                        onClick={() => setActiveTab('news')}
                    >
                        <FileText className="mr-2 h-4 w-4" />
                        News Feed
                    </Button>
                    <Button
                        variant={activeTab === 'groups' ? 'default' : 'ghost'}
                        className="w-full justify-start"
                        onClick={() => setActiveTab('groups')}
                    >
                        <Users className="mr-2 h-4 w-4" />
                        Group Spaces
                    </Button>
                    <Button variant="ghost" className="w-full justify-start">
                        <Settings className="mr-2 h-4 w-4" />
                        Settings
                    </Button>
                    <Button variant="ghost" className="w-full justify-start" onClick={handleLogout}>
                        <LogOut className="mr-2 h-4 w-4" />
                        Logout
                    </Button>
                </nav>
            </div>

            {/* Main Content */}
            <div className="flex-1 flex flex-col overflow-hidden">
                {/* Header */}
                <header className="bg-white shadow-sm">
                    <div className="flex items-center justify-between p-4">
                        <Input type="text" placeholder="Search..." className="w-64" />
                        <div className="flex items-center space-x-4">
                            <Button variant="ghost" size="icon">
                                <Bell className="h-5 w-5" />
                            </Button>
                            <Avatar>
                                <AvatarImage src="https://github.com/shadcn.png" alt="@shadcn" />
                                <AvatarFallback>CN</AvatarFallback>
                            </Avatar>
                        </div>
                    </div>
                </header>

                {/* Content Area */}
                <main className="flex-1 overflow-x-hidden overflow-y-auto bg-gray-100">
                    <div className="container mx-auto px-6 py-8">
                        <h2 className="text-2xl font-semibold text-gray-800 mb-4">
                            {activeTab === 'news' ? 'Company News Feed' : 'Group Spaces'}
                        </h2>
                        <ScrollArea className="h-[calc(100vh-200px)]">
                            {activeTab === 'news' ? (
                                <div className="space-y-4">
                                    {[...Array(10)].map((_, i) => (
                                        <div key={i} className="bg-white rounded-lg shadow p-4">
                                            <h3 className="font-semibold text-lg">Company Announcement {i + 1}</h3>
                                            <p className="text-gray-600 mt-2">
                                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                                            </p>
                                        </div>
                                    ))}
                                </div>
                            ) : (
                                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                                    {[...Array(9)].map((_, i) => (
                                        <div key={i} className="bg-white rounded-lg shadow p-4">
                                            <h3 className="font-semibold text-lg">Group {i + 1}</h3>
                                            <p className="text-gray-600 mt-2">
                                                A space for collaboration and discussion.
                                            </p>
                                            <Button className="mt-4">Join Group</Button>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </ScrollArea>
                    </div>
                </main>
            </div>

            {/* Chat Sidebar */}
            <div className="w-64 bg-white shadow-md">
                <div className="p-4 border-b">
                    <h2 className="text-lg font-semibold">Chat</h2>
                </div>
                <ScrollArea className="h-[calc(100vh-64px)]">
                    <div className="p-4 space-y-4">
                        {[...Array(10)].map((_, i) => (
                            <div key={i} className="flex items-center space-x-3">
                                <Avatar>
                                    <AvatarFallback>{`U${i + 1}`}</AvatarFallback>
                                </Avatar>
                                <div>
                                    <p className="font-medium">User {i + 1}</p>
                                    <p className="text-sm text-gray-500">Online</p>
                                </div>
                            </div>
                        ))}
                    </div>
                </ScrollArea>
            </div>
        </div>
    )
}